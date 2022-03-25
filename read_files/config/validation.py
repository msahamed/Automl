import json
from error_handler import ErrorHandler

class ParameterValidation(object):
    def __init__(self, params= None)->None:
        self.params = params
        self.validate_params()
        self.default_config_path = "./config/default_config.json"
        self.default_params = json.loads(self.default_config_path)
        
    def validate_params(self)->json:
        assert self.params == None, ErrorHandler("Parameter validation", "No parameters provided")
        assert self.params.isinstance(self.params, dict), ErrorHandler("Parameter validation", "Parameters are not in dictionary format")
        assert self.default_params.isinstance(self.default_params, dict), ErrorHandler("Parameter validation", "Default parameters are not in dictionary format")
        
        return self.params
