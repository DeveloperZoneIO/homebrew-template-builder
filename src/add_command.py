# Copyright (c) 2021 Michael Pankraz

import os
from template import Template
from file_manager import FileManager
from template_parser import TemplateParser
from variable import VariableSection, Variable
from script import Script
from content import Content
from base_command import BaseCommand
from config import Config
from input import mockInputs
from io import IO

class AddCommand(BaseCommand):
    '''
    This is the implementation of the template_builders "add" command.
    '''

    def __init__(self):
        BaseCommand.__init__(self, 'add')

    def run(self, arguments, templateBuilder):
        config = Config.load(templateBuilder.configJsonPath)

        if config is None:
            print("No template_builder_config.json found. Please add a template_builder_config.json to the root directory of your project.")

        templateName = self._getTemplateName(arguments)
        templateFilePath = config.localTemplatesPath + templateName + '.tbf'
        templateContent = FileManager().readFileContent(templateFilePath)

        if templateContent is None:
            print('Couldn\'t find template with name: ' + templateName)
            return

        sections = TemplateParser().parseSections(templateContent)
        allVariables = []

        for section in sections:

            # Variable section
            if isinstance(section, VariableSection):
                Executor.askForVariableValues(section)
                allVariables.extend(section.variables)

            # Script section
            elif isinstance(section, Script):
                allVariables = Executor.executeScript(section, allVariables)

            # Content section
            elif isinstance(section, Content):
                workingDirectory = os.getcwd()
                Executor.writeFile(section, allVariables, workingDirectory)

            else:
                print('Unknown section found')

        print('>>> ' + templateName.title() + ' successfully created')
    
    def _getTemplateName(self, arguments):
        '''Retrives the name of the template the user wants to add.'''

        if len(arguments) != 1:
            print('Template name argument missing. Please provide a template name.')
        else:
            return arguments[0]


class Executor:

    @staticmethod
    def _replacePlaceholdersIn(content, variables):
        mutableContent = content

        for var in variables:
            if isinstance(var.value, basestring):
                mutableContent = mutableContent.replace('{{'+ var.name +'}}', var.value)

        return mutableContent

    @staticmethod
    def askForVariableValues(variableSection):
        for variable in variableSection.variables:
            if len(mockInputs) != 0:
                mockValue = mockInputs[0]
                variable.value = mockValue
                mockInputs.remove(mockValue)
            else:
                variable.value = raw_input(variable.prompt + ' ')

    @staticmethod
    def executeScript(scriptSection, variables):
        scriptVariables = {}

        for variable in variables:
            scriptVariables[variable.name] = variable.value
            
        exec(scriptSection.script, scriptVariables)

        extendedVariables = []

        for key, value in scriptVariables.items():
            if key != '__builtins__':
                variable = Variable(key, '')
                variable.value = value
                extendedVariables.append(variable)
    
        return extendedVariables

    @staticmethod
    def writeFile(contentSection, variables, scriptPath):
        contentAndProperties = Executor._replacePlaceholdersIn(contentSection.data, variables)
        properties = {}
        lines = contentAndProperties.split('\n')

        for line in lines:
            strippedLine = line.strip()
            if strippedLine is not '' and strippedLine[0] == '-':
                propName = strippedLine.split('?', 1)[0].strip().replace(' ', '')
                propValue = strippedLine.split('?', 1)[1].strip()
                properties[propName] = propValue

        if '-path' not in properties:
            raise Exception('Missing path? in output section. Please provide a path!')

        path = properties['-path']
        writeMethod = 'replaceExistingFile'

        if '-writeMethod' in properties:
            writeMethod = properties['-writeMethod'].strip()

        propCount = len(properties)
        content = contentAndProperties.split('\n', propCount)[propCount].strip()
        completePath = scriptPath + '/' + path

        IO.write(completePath, content, method=writeMethod)