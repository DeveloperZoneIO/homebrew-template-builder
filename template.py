from variable import Variable
from script import Script
from content import Content

class Template:
    def __init__(self, content):
        self.content = content
        self.parts = content.split('###')
        self.vars = self.parseVariables()
        self.script = self.parseScript()
        self.contents = self.parseContents()

    def getPartWithName(self, partName):
        for part in self.parts:
            if part.split('\n')[0].strip() == partName:
                return part.strip()

    def getAllPartsWithName(self, partName):
        parts = []
        for part in self.parts:
            if part.split('\n')[0].strip() == partName:
                parts.append(part.strip())

        return parts

    def parseVariables(self):
        part = self.getPartWithName('vars')
        lines = part.split('\n')
        lines.remove(lines[0])

        variables = []

        for line in lines:
            varProperties = line.split(':')
            name = varProperties[0].strip()
            prompt = varProperties[1].strip()
            variable = Variable(name, prompt)
            variables.append(variable)

        return variables

    def parseScript(self):
        part = self.getPartWithName('py_script')
        headerAndScript = part.split('\n', 1)
        return Script(headerAndScript[1])

    def parseContents(self):
        contentParts = self.getAllPartsWithName('content')

        contents = []

        for contentPart in contentParts:
            contents.append(Content(contentPart))

        return contents
