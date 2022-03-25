import sys
import logging
from datetime import date

log = logging.getLogger(__name__)

class ErrorHandler(object):
    def __init__(self, error_location, message, exit = False):
        self.header = "Error"
        self.error_location = error_location
        self.message = message
        self.exit = exit
        self.print_error()

    def print_error(self)->None:
        log.info(f'\n--------------- {self.header} -------------------\
                \nError location: {self.error_location}\
                \nError message: {self.message}\
                \nError Time: {date.today().strftime("%B %d, %Y %H:%M:%S")}\
                \n--------------------------------------------')
        self.exit_program()
        
    def exit_program(self)->None:
        if self.exit:
            print(f'\n--------------- {self.header} -------------------\
                \nError location: {self.error_location}\
                \nError message: {self.message}\
                \nError Time: {date.today().strftime("%B %d, %Y %H:%M:%S")}\
                \n--------------------------------------------')
            sys.exit(99)