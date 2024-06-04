class Variable:
    def __init__(self, name, domain, val=None):
        self.name = name
        self.domain = domain
        self.val = val

    def __eq__(self, other):
        return self.name == other.name


