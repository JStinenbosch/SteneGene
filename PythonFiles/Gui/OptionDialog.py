from PyQt5.QtWidgets import *

from PythonFiles.Gui.OptionWidgets.MultiFileSelectorWidget import MultiFileSelectorWidget


class OptionDialog(QDialog):
    def __init__(self, required):
        super().__init__()

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.buildFileSelection(required["files"])
        self.buildChoices(required["choices"])
        self.buildFlags(required["flags"])

        self.show()

    def buildFileSelection(self, fileSelectors):
        self.fileGrid = QGridLayout()
        number = 0
        for selector in fileSelectors:
            if selector["type"] == "multi":
                widget = MultiFileSelectorWidget()
                self.fileGrid.addWidget(widget, number, 1)
            elif selector["type"] == "single":
                print("Flikker op")
                #self.buildSingleFileSelector()

        self.grid.addLayout(self.fileGrid, 1, 1)

    def buildChoices(self, choices):
        self.choiceGrid = QGridLayout()
        number = 0
        for choice in choices:
            label = QLabel(choice["name"])
            combobox = QComboBox()
            for option in choice["options"]:
                combobox.addItem(option)
            self.choiceGrid.addWidget(label, number, 1)
            self.choiceGrid.addWidget(combobox, number, 2)
            number += 1

        self.grid.addLayout(self.choiceGrid, 2, 1)

    def buildFlags(self, flags):
        self.flagGrid = QGridLayout()
        number = 0
        for flag in flags:
            checkBox = QCheckBox(flag["name"])
            checkBox.setChecked(flag["state"])
            xPos = number % 4
            yPos = number / 4
            self.flagGrid.addWidget(checkBox, yPos, xPos)
            number += 1

        self.grid.addLayout(self.flagGrid, 3, 1)

