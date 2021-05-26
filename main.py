#!/usr/bin/python

import sys
import os
from src.template_builder import TemplateBuilder

workingDirectory = os.getcwd()
configPath = workingDirectory + '/template_builder_config.json'
TemplateBuilder.run(sys.argv, configPath)

# TODOs:
# - add writeFile? True/False to content properties
# - add overrideExistingFile? True/False to content properties
# - replace variable : separator with ?