import os
import errno
from variable import Variable

class ContentSettings:
    def __init__(self):
        self.overrideExisting = True
        self.path = 'root_directory'

class Content:
    def __init__(self, data):
        self.data = data

    def replacePlaceholdersIn(self, content, variables):
        mutableContent = content

        for var in variables:
            mutableContent = mutableContent.replace('{{'+ var.name +'}}', var.value)

        return mutableContent

    def writeFile(self, variables, scriptPath):
        path = self.data.split('\n', 1)[0].strip()
        content = self.data.split('\n', 1)[1].strip()

        if 'path:' not in path:
            path = '/'
            content = self.data.split('\n', 2)[1].strip()
        else:
            path = path.split(':')[1].strip()

        finalPath = self.replacePlaceholdersIn(path, variables)
        finalContent = self.replacePlaceholdersIn(content, variables)
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
