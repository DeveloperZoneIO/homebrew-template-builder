# Copyright (c) 2021 Michael Pankraz

import os
from base_command import BaseCommand

class InitCommand(BaseCommand):

    def __init__(self):
        BaseCommand.__init__(self, 'init')

    def run(self, arguments, templateBuilder):
        workingDirectory = os.getcwd()
        baseConfig = '''
{
    "localTemplates": {
        "path": "templates/"
    }
}
        '''

        file = open(workingDirectory + '/template_builder_config.json', 'w')
        file.write(baseConfig)
        file.close()