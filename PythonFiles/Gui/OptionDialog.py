from PyQt5.QtWidgets import *

from PythonFiles.Gui.OptionWidgets.ChoiceWidget import ChoiceWidget
from PythonFiles.Gui.OptionWidgets.FlagWidget import FlagWidget
from PythonFiles.Gui.OptionWidgets.MultiFileSelectorWidget import MultiFileSelectorWidget
from PythonFiles.Gui.OptionWidgets.SingleFileSelectorWidget import SingleFileSelectorWidget


class OptionDialog(QDialog):
    def __init__(self, required):
        super().__init__()

        self.required = required
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.widgets = {}

        self.build()

        self.show()

    def build(self):
        position = 1
        for option in self.required:
            option_type = option["type"]
            option_id = option["id"]
            option_info = option["info"]
            if option_type == "choice" :
                widget = ChoiceWidget(option_info)
            elif option_type == "flags" :
                widget = FlagWidget(option_info)
            elif option_type == "multi_file":
                widget = MultiFileSelectorWidget()
            elif option_type == "single_file":
                widget = SingleFileSelectorWidget()

            self.widgets[option_id] = widget
            self.grid.addWidget(widget, position, 1)
            position += 1

    def result(self):
        result_dict = {}
        for _id in self.widgets:
            widget = self.widgets[_id]
            result_dict[_id] = widget.result()

        return result_dict


