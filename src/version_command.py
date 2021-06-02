# Copyright (c) 2021 Michael Pankraz

from base_command import BaseCommand
import script_properties

class VersionCommand(BaseCommand):
    '''
    This is the implementation of the template_builders "version" command.
    '''

    def __init__(self):
        BaseCommand.__init__(self, 'version')

    def run(self, arguments, tempateBuilder):
        print('template_builder ' + script_properties.versionName)