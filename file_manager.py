import sys
import os

# Reads and writes files.
class FileManager:
    def __init__(self):
        pass

    def readFileContent(self, filePath):
        if os.path.isfile(filePath) != True: 
            return

        file = open(filePath)
        fileContent = file.read()
        file.close()
        return fileContent

    def writeFile(self):
        pass