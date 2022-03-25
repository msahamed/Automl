''''
Author: Sabber Ahamed
Email: sabbers@gmail.com
Linkedin: https://www.linkedin.com/in/sabber-ahamed/

Purpose of this file:
-----------------------
This file is used to read the config file and return the configs as a dictionary.

'''

import json
from error_handler import ErrorHandler
from .validation import ParameterValidation

class ReadConfigFile(object):
    def __init__(self, file_path: str = None)->None:
        self.file_path = file_path
        self.read_config_file()
    
    def read_config_file(self):
        '''
        the purpose of this function is to read the config file and return the configs as a dictionary.
        '''
        assert self.file_path == None, ErrorHandler("Reading config file", "File path is not provided", True)
        
        with open(self.file_path, 'r') as f:
            self.config_params = dict(json.load(f))
            self.config_params = ParameterValidation(self.config_params)
            
        