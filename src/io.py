# Copyright (c) 2021 Michael Pankraz

import os

class IO:
    @staticmethod
    def write(path, content, method='replaceExistingFile'):
        if method == 'none':
            return

        IO._createDirectoryIfNotExist(path)

        if method == 'replaceExistingFile':
            IO._justWriteFile(path, content)
            return


        if method == 'keepExistingFile':
            if os.path.exists(path):
                return
            else:
                IO._justWriteFile(path, content)
                return

        if method == 'extendExistingFile':
            if not os.path.exists:
                IO._justWriteFile(path, content)
                return
            else:
                existingContent = IO.read(path)
                newContent = existingContent + '\n' + content
                IO._justWriteFile(path, newContent)
                return

    @staticmethod
    def read(path):
        if os.path.isfile(path) != True: 
            raise Exception('File at ' + path + ' doesn\'t exist!')

        file = open(path)
        fileContent = file.read()
        file.close()

        return fileContent

    @staticmethod
    def _justWriteFile(path, content):
        file = open(path, 'w')
        file.write(content)
        file.close()

    @staticmethod
    def _createDirectoryIfNotExist(path):
        directoryPath = os.path.dirname(path)

        if os.path.exists(directoryPath):
            return
        
        try:
            os.makedirs(directoryPath)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise
