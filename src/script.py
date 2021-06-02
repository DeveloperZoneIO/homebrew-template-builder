# Copyright (c) 2021 Michael Pankraz

from variable import Variable

class Script:
    def __init__(self, script):
        self.script = script
        
    def execute(self, variables):
        scriptVariables = {}

        for var in variables:
            scriptVariables[var.name] = var.value
            
        exec(self.script, scriptVariables)

        extendedVariables = []

        for key, value in scriptVariables.items():
            if key != '__builtins__':
                variable = Variable(key, '')
                variable.value = value
                extendedVariables.append(variable)
    
        return extendedVariables

        
