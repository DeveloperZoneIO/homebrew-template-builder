from template_builder import TemplateBuilder
from file_manager import FileManager
from config import Config
from input import addMockInput

import unittest
import os
import shutil

class AddOperationTest(unittest.TestCase):

    def test_content_only(self):
        AddOperationTest._runTemplateBuilder(
            arguments=['template_builder.py', 'add', 'content_only'],
        )

        expected = 'Some random content'
        actual = AddOperationTest._readFile('content_only.txt')
        self.assertEqual(expected, actual)
        AddOperationTest._clean()

    def test_dont_write_content(self):
        AddOperationTest._runTemplateBuilder(
            arguments=['template_builder.py', 'add', 'dont_write_content'],
        )

        actual = AddOperationTest._readFileSave('dont_wirte_content.txt')
        self.assertEqual(None, actual)
        AddOperationTest._clean()

    def test_content_with_single_var(self):
        AddOperationTest._runTemplateBuilder(
            arguments=['template_builder.py', 'add', 'content_with_single_var'],
            inputs=['Hello template builder :)']
        )

        expected = 'Your random input is: Hello template builder :)\nYour inputs variable is named someInput'
        actual = AddOperationTest._readFile('single_var_and_content.txt')
        self.assertEqual(expected, actual)
        AddOperationTest._clean()

    def test_content_with_multiple_vars(self):
        AddOperationTest._runTemplateBuilder(
            arguments=['template_builder.py', 'add', 'content_with_mutliple_vars'],
            inputs=['test', 'Hello', 'world!']
        )

        expected = 'Hello\nworld!'
        actual = AddOperationTest._readFile('test.txt')
        self.assertEqual(expected, actual)

        AddOperationTest._clean()

    def test_multiple_content_with_multiple_vars(self):
        AddOperationTest._runTemplateBuilder(
            arguments=['template_builder.py', 'add', 'multiple_content_with_mutliple_vars'],
            inputs=['multiple_content_with_mutliple_vars', 'Hello', 'world!']
        )

        expected = 'Hello\nworld!'
        self.assertEqual(expected, AddOperationTest._readFile('multiple_content_with_mutliple_vars1.txt'))
        self.assertEqual(expected, AddOperationTest._readFile('multiple_content_with_mutliple_vars2.txt'))
        self.assertEqual(expected, AddOperationTest._readFile('multiple_content_with_mutliple_vars3.txt'))

        AddOperationTest._clean()

    def test_script(self):
        AddOperationTest._runTemplateBuilder(
            arguments=['template_builder.py', 'add', 'movie'],
            inputs=['title', '01/01/01', '8.5']
        )

        expected = 'title (8.5)\nReleased on 01.01.01'
        actual = AddOperationTest._readFile('movies/title.txt')
        self.assertEqual(expected, actual)

        AddOperationTest._clean()

    @staticmethod
    def _clean():
        shutil.rmtree('src/test_generated/', ignore_errors=True)

    @staticmethod
    def _runTemplateBuilder(arguments=[], inputs=[]):
        workingDirectory = os.getcwd()
        configPath = workingDirectory + '/src/test_config.json'

        for inputValue in inputs:
            addMockInput(inputValue)
        
        TemplateBuilder.run(arguments, configPath)

    @staticmethod
    def _readFile(fileName):
        return FileManager().readFileContent(os.getcwd() + '/src/test_generated/' + fileName)

    @staticmethod
    def _readFileSave(fileName):
        return FileManager().readFileContentSafe(os.getcwd() + '/src/test_generated/' + fileName)

if __name__ == '__main__':
    unittest.main()