# Copyright (c) 2021 Michael Pankraz

from add_command import AddCommand
from init_command import InitCommand
from config import Config

class TemplateBuilder:
    def __init__(self):
        self.configJsonPath = None

    def run(self, arguments):
        allOperations = [
            AddCommand(),
            InitCommand(),
        ]

        if len(arguments) <= 1:
            print('Missing operation! Please provide one of the following arguments to template_builder:')
            print('- add')
        else:
            selectedOperation = arguments[1]
            operationArguments = arguments[2:] or []

            didFoundOperation = False

            for operation in allOperations:
                if operation.identifier == selectedOperation:
                    operation.run(operationArguments, self)
                    didFoundOperation = True

            if not didFoundOperation:
                print(selectedOperation + ' is not defined.')