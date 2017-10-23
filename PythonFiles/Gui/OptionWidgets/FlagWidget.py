from PyQt5.QtWidgets import *


class FlagWidget(QWidget):
    def __init__(self, options):
        super().__init__()
        self.flags = options["flags"]

        self.build()

    def build(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.checkBoxes = {}
        number = 0
        for flag in self.flags:
            checkBox = QCheckBox(flag["name"])
            checkBox.setChecked(flag["state"])
            xPos = number % 4
            yPos = number / 4
            grid.addWidget(checkBox, yPos, xPos)
            self.checkBoxes[flag["name"]] = checkBox
            number += 1

    def result(self):
        result_flags = []
        for flag in self.flags:
            checkbox = self.checkBoxes[flag["name"]]
            result_flags.append({"name": flag["name"], "state" : checkbox.checkState()})

        return result_flags