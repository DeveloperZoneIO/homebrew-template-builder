# Copyright (c) 2021 Michael Pankraz

from add_command import AddCommand
from init_command import InitCommand
from version_command import VersionCommand
from config import Config

class TemplateBuilder:
    def __init__(self):
        self.configJsonPath = None

    def run(self, arguments):
        allOperations = [
            AddCommand(),
            InitCommand(),
            VersionCommand(),
        ]

        if len(arguments) <= 1:
            commandNames = []

            for command in allOperations:
                commandNames.append('* ' + command.identifier)

            print('Missing command!\nPlease provide one of the following arguments:')
            print('\n'.join(commandNames))
            # Bash commands not implemented in python
            print('* update')
            print('* uninstall')
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