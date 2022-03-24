import time
import logging
import dask as dd
from error_handler import ErrorHandler
log = logging.getLogger(__name__)


class ReadCSVFile(object):
    def __init__(self, file_path: str, target:str)->None:
        self.file_path = file_path
        self.target = target
    
    def read_data(self, path: str)->dd.DataFrame:
        start_time = time.time()
        assert self.file_path, 'Data file path is not provided'

        try:
            df = dd.read_csv(self.file_path)
            log.info(f'Finished reading data\
            \nFile path {path}\
            \nShape of the data: {df.shape}\
            \nTime to read the file: {time.time()-start_time}')
            return df
        except Exception as e:
            ErrorHandler("Reading data in read_file.py", e, True)

