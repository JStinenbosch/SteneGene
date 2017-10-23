'''
    File name:      Controller.py
    Python Version: 3.5
    Description:    This file contains the controller, which serves as the bridge between the GUI and the pipeline of
                    biological programs. 
'''
import sys
from PyQt5.QtWidgets import QApplication

from PythonFiles.BlastBuilder import BlastBuilder
from PythonFiles.Gui.MainWindow import MainWindow


class Controller(object):

    def __init__(self):
        self.view = MainWindow(self)
        self.model = BlastBuilder()
        self.view.run()


    def set_WGS(self, parameter_dict: dict):
        self.model.set_WGS_paths(parameter_dict["WGS_path"])
        self.model.set_WGS_flags(parameter_dict["seq_type"])

    def set_query(self, parameter_dict: dict):
        self.model.set_query_paths(parameter_dict["query_path"])
        self.model.set_query_flags(parameter_dict["seq_type"])

    def set_blast_param(self, parameter_dict: dict):
        self.model.set_blast_param(parameter_dict)

    def set_output_file(self, target_output: str):
        self.model.set_output_file(target_output)

    def run_blast(self):
        self.model.run_blast()

    def can_run(self):
        print(self.model.is_runnable())
        return self.model.is_runnable()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Controller()
    sys.exit(app.exec_())
