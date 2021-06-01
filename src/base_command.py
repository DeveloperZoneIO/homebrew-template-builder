# Copyright (c) 2021 Michael Pankraz

class BaseCommand:
    '''
    This serves as the base class for all template_builder commands.
    
    Parameters
    ----------
    identifier : str
        the identifier of the command

    Attributes
    ----------
    identifier : str
        the identifier of the command
    '''

    def __init__(self, identifier):
        self.identifier = identifier

    def run(self, arguments, templateBuilder):
        '''
        Starts the command. Should be implemented by the inheriting class.

        Parameters
        ----------
        arguments : [str]
            the arguments from the command line for the command.

        templateBuilder : TemplateBuilder
            the template builder instance currenly running.
        '''
        pass