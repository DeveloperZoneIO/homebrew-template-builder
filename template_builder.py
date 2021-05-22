#!/usr/bin/python

import sys
from add_operation import AddOperation

allOperations = [
    AddOperation(),
]

if len(sys.argv) <= 1:
    print('Missing operation! Please provide one of the following arguments to template_builder:')
    print('- add')
else:
    selectedOperation = sys.argv[1]
    operationArguments = sys.argv[2:] or []

    didFoundOperation = False

    for operation in allOperations:
        if operation.identifier == selectedOperation:
            operation.run(operationArguments)
            didFoundOperation = True

    if not didFoundOperation:
        print(selectedOperation + ' is not defined.')
        