from PyQt5.QtWidgets import *


class InputWidget(QWidget):
    def __init__(self, input):
        super().__init__()
        self.input = input

        self.build()

    def build(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.choiceComboBoxes = {}
        label = QLabel(self.input["label"])
        self.input_field = QLineEdit(self.input["default"])
        grid.addWidget(label, 1, 1)
        grid.addWidget(self.input_field, 1, 2)


    def result(self):
        return {"label" : self.input["label"], "value" : self.input_field.text()}