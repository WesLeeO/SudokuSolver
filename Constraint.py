class Constraint:
    def __init__(self, variables):
        self.variables = variables

    def dimension(self):
        return len(self.variables)