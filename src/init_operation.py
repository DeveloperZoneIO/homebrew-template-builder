import os
from opearation import Operation

class InitOperation(Operation):

    def __init__(self):
        Operation.__init__(self, 'init')

    def run(self, arguments):
        workingDirectory = os.getcwd()
        baseConfig = '''
{
    "localTemplates": {
        "path": "templates/"
    }
}
        '''

        # fileDir = os.path.dirname(completePath)

        # if not os.path.exists(fileDir):
        #     try:
        #         os.makedirs(fileDir)
        #     except OSError as exc:
        #         if exc.errno != errno.EEXIST:
        #             raise

        # if os.path.isfile(completePath) and replaceExistingFile != 'true':
        #     return

        file = open(workingDirectory + '/template_builder_config.json', 'w')
        file.write(baseConfig)
        file.close()