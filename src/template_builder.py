
from add_operation import AddOperation
from init_operation import InitOperation
from config import Config

class TemplateBuilder:

    @staticmethod
    def run(arguments):
        allOperations = [
            AddOperation(),
            InitOperation(),
        ]

        # TODO: Add documentation to readme.md

        if len(arguments) <= 1:
            print('Missing operation! Please provide one of the following arguments to template_builder:')
            print('- add')
        else:
            selectedOperation = arguments[1]
            operationArguments = arguments[2:] or []

            didFoundOperation = False

            for operation in allOperations:
                if operation.identifier == selectedOperation:
                    operation.run(operationArguments)
                    didFoundOperation = True

            if not didFoundOperation:
                print(selectedOperation + ' is not defined.')