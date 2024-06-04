from constraint.BinaryConstraint import BinaryConstraint
from model.PSC import PSC
from var.VariableWithLabel import VariableWithLabel


class Sudoku:

    # Grid is a 2D array with initial values or None
    def __init__(self, grid, size=9):
        self.constraints = None
        self.size = size
        variables = []
        for row in range(self.size):
            for col in range(self.size):
                if grid[row][col] != 0:
                    var = VariableWithLabel(name="R{}C{}".format(row + 1, col + 1),
                                            domain=[grid[row][col]],
                                            val=grid[row][col])
                else:
                    var = VariableWithLabel(name="R{}C{}".format(row + 1, col + 1),
                                            domain=list(range(1, self.size + 1)))
                variables.append(var)
        self.variables = variables
        self.find_constraints()

    def find_constraints(self):
        constraints = []
        for row in range(self.size):
            for col in range(self.size):

                # Rows
                for rightCol in range(col + 1, self.size):
                    c = BinaryConstraint(self.variables[row * self.size + col],
                                         self.variables[row * self.size + rightCol],
                                         lambda x, y: x != y)
                    constraints.append(c)
                # Columns
                for lowerRow in range(row + 1, self.size):
                    c = BinaryConstraint(self.variables[row * self.size + col],
                                         self.variables[lowerRow * self.size + col],
                                         lambda x, y: x != y)
                    constraints.append(c)
                # Squares
                # Only called for upper left corners
                if row % 3 == 0 and col % 3 == 0:
                    # constraints for diagonals
                    for row1 in range(row, row + int(self.size / 3), 1):
                        for col1 in range(col, col + int(self.size / 3), 1):
                            for row2 in range(row, row + int(self.size / 3), 1):
                                for col2 in range(col, col + int(self.size / 3), 1):
                                    if row1 != row2 and col1 != col2 and row1 < row2:
                                        c = BinaryConstraint(self.variables[row1 * self.size + col1],
                                                             self.variables[row2 * self.size + col2],
                                                             lambda x, y: x != y)
                                        constraints.append(c)
                self.constraints = constraints

    def solve(self):
        psc = PSC(self.variables, self.constraints)
        psc.consistency()
        psc.forward_checking(one_solution=True)
        for row in range(self.size):
            for col in range(self.size):
                name = self.variables[row * self.size + col].name
                self.variables[row * self.size + col].val = psc.solutions[0][name]

    def __repr__(self):
        ret = ''
        for row in range(self.size):
            for col in range(self.size):
                ret += '{} '.format(self.variables[row * self.size + col].val)
            ret += '\n'
        return ret

