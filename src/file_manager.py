import sys
import os

# Reads and writes files.
class FileManager:
    def __init__(self):
        pass

    def readFileContent(self, filePath):
        if os.path.isfile(filePath) != True: 
            raise Exception(filePath + ' is no file!')

        file = open(filePath)
        fileContent = file.read()
        file.close()
        return fileContent

    def readFileContentSafe(self, filePath):
        if os.path.isfile(filePath) != True: 
            return None

        file = open(filePath)
        fileContent = file.read()
        file.close()
        return fileContent

    def writeFile(self):
        pass