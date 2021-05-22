import os
from file_manager import FileManager
import json

class Config:
    def __init__(self):
        self.localTemplateDirectoryPath = None
        self.remoteTemplateDirectoryPath = None

    @staticmethod
    def load():
        workingDirectory = os.getcwd()
        configContent = FileManager().readFileContent(workingDirectory + '/template_builder_config.json')
        configDict = json.loads(configContent)

        config = Config()
        config.localTemplateDirectoryPath = configDict['template']['local_template_folder_path']
        config.remoteTemplateDirectoryPath = configDict['template']['remote_template_folder_path']

        return config


