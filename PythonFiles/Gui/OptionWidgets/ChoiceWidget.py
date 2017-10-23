from PyQt5.QtWidgets import *


class ChoiceWidget(QWidget):
    def __init__(self, choice):
        super().__init__()
        self.choice = choice

        self.build()

    def build(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.choiceComboBoxes = {}
        label = QLabel(self.choice["label"])
        self.combobox = QComboBox()
        for option in self.choice["options"]:
            self.combobox.addItem(option)
        grid.addWidget(label, 1, 1)
        grid.addWidget(self.combobox, 1, 2)


    def result(self):
        return self.combobox.currentText()