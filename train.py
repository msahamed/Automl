
import numpy as np
import pandas as pd
from get_data import ReadData

class AutoML(object):
    def __init__(self, config_file_path):
        self.config_file = read_config_file(config_file_path)
        pass
    def fit(self):
        pass
        # get data
        # Preprocess and clean data
        # Split data into train and test
        # Visualize data
        # train models
        # find best model
        # display results (visulaize)
        
if __name__ == '__main__':
    automl = AutoML(config_file_path=sys.argv[1])
    automl.fit()
