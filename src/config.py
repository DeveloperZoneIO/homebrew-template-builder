# Copyright (c) 2021 Michael Pankraz

from file_manager import FileManager
import json

class Config:
    def __init__(self):
        self.localTemplatesPath = None

    @staticmethod
    def load(configPath):
        configContent = FileManager().readFileContent(configPath)
        configDict = json.loads(configContent)

        config = Config()
        Config._parseLocalTemplateProperties(configDict, config)

        return config

    @staticmethod
    def _parseLocalTemplateProperties(configDict, config):
        if 'localTemplates' not in configDict:
            raise Exception('Missing localeTemplate part in configuration.')
        
        localTemplatesConfig = configDict['localTemplates']

        if 'path' in localTemplatesConfig:
            config.localTemplatesPath = localTemplatesConfig['path']
        else:
            raise Exception('Missing path for localTemplates.')