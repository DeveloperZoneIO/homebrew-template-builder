#!/usr/bin/python

import sys
import os
from src.template_builder import TemplateBuilder

workingDirectory = os.getcwd()

tb = TemplateBuilder()
tb.configJsonPath = workingDirectory + '/template_builder_config.json'
tb.run(sys.argv)