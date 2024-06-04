from Variable import Variable


class VariableWithLabel(Variable):

    def __init__(self, name, domain, val=None):
        Variable.__init__(self, name, domain, val)
        self.label = domain



