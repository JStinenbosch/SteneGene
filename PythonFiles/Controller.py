'''
    File name:      Controller.py
    Python Version: 3.5
    Description:    This file contains the controller, which serves as the bridge between the GUI and the pipeline of
                    biological programs. 
'''

class Controller(object):
    # The controller needs a method to read the command which is sent to it by the GUI. We parse the pipeline arguments
    # and call the correct methods in the object.
    def parse_arguments(self):
        return None

    # This method starts one of the BLAST programs
    def start_BLAST(self, wgs, query, arguments):
        return None
