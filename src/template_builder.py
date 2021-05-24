
from add_operation import AddOperation
from config import Config

class TemplateBuilder:

    @staticmethod
    def run(arguments, configPath):
        allOperations = [
            AddOperation(),
        ]

        # TODO: Add documentation to readme.md

        if configPath is None:
            print("No template_builder_config.json found. Please add a template_builder_config.json to the root directory of your project.")
        else:
            config = Config.load(configPath)

        if config is None:
            print("No template_builder_config.json found. Please add a template_builder_config.json to the root directory of your project.")
        elif len(arguments) <= 1:
            print('Missing operation! Please provide one of the following arguments to template_builder:')
            print('- add')
        else:
            selectedOperation = arguments[1]
            operationArguments = arguments[2:] or []

            didFoundOperation = False

            for operation in allOperations:
                if operation.identifier == selectedOperation:
                    operation.run(operationArguments, config)
                    didFoundOperation = True

            if not didFoundOperation:
                print(selectedOperation + ' is not defined.')