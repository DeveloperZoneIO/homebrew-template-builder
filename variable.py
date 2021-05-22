class VariableSection:
    def __init__(self, variables):
        self.variables = variables

class Variable:
    def __init__(self, name, prompt):
        self.name = name
        self.prompt = prompt
        self.value = 'undefined'

    def prnt(self):
        if self.name is not None:
            print('var.name: '+ str(self.name))

        if self.prompt is not None:
            print('var.prompt: '+ str(self.prompt))

        if self.value is not None:
            print('var.value: '+ str(self.value))