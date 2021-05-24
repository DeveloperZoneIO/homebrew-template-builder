class Operation:
    def __init__(self, identifier):
        self.identifier = identifier

    def run(self, arguments, config):
        self.config = config
        self.arguments = arguments