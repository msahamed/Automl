import os
import logging

log = logging.getLogger(__name__)

class ErrorHander(object):
    def __init__(self, error_location, message, is_exit = False):
        self.error_location = error_location
        self.message = message
        self.is_exit = is_exit

    def print_error(self)->None:
        header = 'Error'

        log.info(f'\n--------------- {header} -------------------\
                \n{self.error_location}\
                \n{self.message}\
                \n--------------------------------------------')
        self.exit_program()
        
    def exit_program(self)->None:
        if self.is_exit:
            os._exit(99)