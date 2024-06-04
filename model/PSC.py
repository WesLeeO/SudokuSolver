class PSC:

    def __init__(self, variables, constraints):
        self.solutions = []
        self.variables = variables
        self.constraints = constraints

    def consistency(self):
        modified = True
        while modified:
            modified = False
            for c in self.constraints:
                if c.Waltz():
                    modified = True

        for var in self.variables:
            var.label = var.domain[:]
            var.val = None

    def consistant_propagation(self, k):
        fc = [c for c in self.constraints if self.variables[k] in c.variables]
        for c in fc:
            emptyLabel = c.propagate(self.variables[k])
            if emptyLabel:
                return False
        return True

    def forward_checking(self, k=0, one_solution=False):
        if k >= len(self.variables):
            if not one_solution:
                solution = {var.name: var.val for var in self.variables}
                self.solutions.append(solution)

            else:
                solution = {var.name: var.val for var in self.variables}
                self.solutions.append(solution)
                return self.solutions
        else:
            var = self.variables[k]
            labelCopy = var.label.copy()
            labels = []

            for i in range(k + 1, len(self.variables)):
                labels.append((self.variables[i].name, self.variables[i].label.copy()))

            for val in labelCopy:
                var.val = val
                var.label = [val]
                res = self.consistant_propagation(k)
                if res:
                    remaining = self.forward_checking(k + 1, one_solution)
                    if remaining != 'failure':
                        return remaining
                for i in range(k + 1, len(self.variables)):
                    self.variables[i].label = labels[i - k - 1][1]
                    self.variables[i].val = None
        return 'failure'
