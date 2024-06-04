from constraint.Constraint import Constraint


class BinaryConstraint(Constraint):

    def __init__(self, var1, var2, op):
        Constraint.__init__(self, [var1, var2])
        self.op = op

    def isValid(self):
        return self.op(self.variables[0].val, self.variables[1].val)

    def isPossible(self, var):
        for value in var.domain:
            var.val = value
            if self.isValid():
                return True
        return False

    # Reduce the domain (initially called based on initial settings)
    def Waltz(self):
        modified0 = self.Waltz0(self.variables[0], self.variables[1])
        modified1 = self.Waltz0(self.variables[1], self.variables[0])
        changed = modified0 or modified1
        if changed:
            self.variables[0].label = self.variables[0].domain
            self.variables[1].label = self.variables[1].domain
        return changed

    def Waltz0(self, var, varToReduce):
        toBeRemoved = []
        changed = False
        for value in varToReduce.domain:
            varToReduce.val = value
            if self.isPossible(var):
                continue
            else:
                toBeRemoved.append(value)
                changed = True
        varToReduce.domain = [value for value in varToReduce.domain if value not in toBeRemoved]
        return changed

    # Reduce labels (call during DFS search)
    def propagate(self, var):
        emptyLabel = True
        toBeRemoved = []
        if self.variables[0].name == var.name:
            for value in self.variables[1].label:
                self.variables[1].val = value
                if not self.isValid():
                    toBeRemoved.append(value)
                else:
                    emptyLabel = False
            self.variables[1].label = [value for value in self.variables[1].label if value not in toBeRemoved]
        else:
            for value in self.variables[0].label:
                self.variables[0].val = value
                if not self.isValid():
                    toBeRemoved.append(value)
                else:
                    emptyLabel = False
            self.variables[0].label = [value for value in self.variables[0].label if value not in toBeRemoved]
        return emptyLabel
