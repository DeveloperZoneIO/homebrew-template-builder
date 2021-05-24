
import os
from template import Template
from file_manager import FileManager
from template_parser import TemplateParser
from variable import VariableSection, Variable
from script import Script
from content import Content
from opearation import Operation
from config import Config
from input import mockInputs

class AddOperation(Operation):

    def __init__(self):
        Operation.__init__(self, 'add')

    def getTemplateName(self, arguments):
        if len(arguments) != 1:
            print('Template name argument missing. Please provide a template name.')
        else:
            return arguments[0]

    def run(self, arguments, config):
        workingDirectory = os.getcwd()
        templateName = self.getTemplateName(arguments)
        filePath = config.localTemplatesPath + templateName + '.tbf'
        templateContent = FileManager().readFileContent(filePath)

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
                Executor.writeFile(section, allVariables, workingDirectory)

            else:
                print('Unknown section found')

        print('>>> ' + templateName.title() + ' successfully created')


class Executor:

    @staticmethod
    def _replacePlaceholdersIn(content, variables):
        mutableContent = content

        for var in variables:
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
                variable.value = raw_input(variable.prompt + ': ')

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
        path = contentSection.data.split('\n', 1)[0].strip()
        content = contentSection.data.split('\n', 1)[1].strip()

        if 'path:' not in path:
            path = '/'
            content = contentSection.data.split('\n', 2)[1].strip()
        else:
            path = path.split(':')[1].strip()

        finalPath = Executor._replacePlaceholdersIn(path, variables)
        finalContent = Executor._replacePlaceholdersIn(content, variables)
        completePath = scriptPath + finalPath
        fileDir = os.path.dirname(scriptPath + finalPath)

        if not os.path.exists(fileDir):
            try:
                os.makedirs(fileDir)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

        file = open(completePath, 'w')
        file.write(finalContent)
        file.close()
