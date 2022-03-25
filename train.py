import sys, os
from read_files.data import ReadCSVFile
from read_files.config import ReadConfigFile
from error_handler import ErrorHandler

class AutoML(object):
    def __init__(self, config_file_path):        
        self.configs = ReadConfigFile(config_file_path)
        
    def fit(self):
        pass
        # get data
        # Preprocess and clean data
        # Split data into train and test
        # Visualize data
        # train models
        # find best model
        # display results (visualize)
        
if __name__ == '__main__':
    print(len(sys.argv))
    
    if len(sys.argv) == 1:
        ErrorHandler("AutoML", "Config file is not provided", True)
    
    config_file = sys.argv[1]
    automl = AutoML(config_file_path=config_file)
    automl.fit()
