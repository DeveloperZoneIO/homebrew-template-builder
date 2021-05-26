from variable import Variable, VariableSection
from script import Script
from content import Content

class TemplateParser:
    def parseSections(self, templateContent):
        sectionContents = templateContent.split('@_')
        sectionObjects = []

        for sectionContent in sectionContents:
            sectionObject = self._createSectionObject(sectionContent)

            if sectionObject is not None:
                sectionObjects.append(sectionObject)

        return sectionObjects

    def _createSectionObject(self, section):
        if section.strip() == '':
            return None

        sectionNameAndContent = section.split('\n', 1)
        sectionName = sectionNameAndContent[0].strip().lower()
        sectionContent = sectionNameAndContent[1]

        if sectionName == 'input':
            return self._parseVariableSection(sectionContent)
        elif sectionName == 'script':
            return self._parseScriptSection(sectionContent)
        elif sectionName == 'output':
            return self._parseTemplateSection(sectionContent)
        else:
            print('Invalid section name: ' + sectionName)
            return None

    def _parseVariableSection(self, content):
        lines = content.split('\n')
        variables = []

        for line in lines:
            nameAndPrompt = line.split('?', 1)

            if len(nameAndPrompt) == 2 and nameAndPrompt[0].strip() != '':
                name = nameAndPrompt[0].strip()
                prompt = nameAndPrompt[1].strip()
                variable = Variable(name, prompt)
                variables.append(variable)

        return VariableSection(variables)

    def _parseScriptSection(self, content):
        return Script(content)

    def _parseTemplateSection(self, content):
        return Content(content)