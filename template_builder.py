#!/usr/bin/python

import sys
from add_operation import AddOperation
from config import Config

allOperations = [
    AddOperation(),
]

config = Config.load()

if config is None:
    print("No template_builder_config.json found. Please add a template_builder_config.json to the projects root directory.")
elif len(sys.argv) <= 1:
    print('Missing operation! Please provide one of the following arguments to template_builder:')
    print('- add')
else:
    selectedOperation = sys.argv[1]
    operationArguments = sys.argv[2:] or []

    didFoundOperation = False

    for operation in allOperations:
        if operation.identifier == selectedOperation:
            operation.run(operationArguments, config)
            didFoundOperation = True

    if not didFoundOperation:
        print(selectedOperation + ' is not defined.')
        