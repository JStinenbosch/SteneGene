from PyQt5.QtWidgets import *

from PythonFiles.Gui.OptionDialog import OptionDialog


class PipelineWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.WGSButton = QPushButton("WGS")
        self.WGSButton.clicked.connect(lambda: self.onButtonClicked(self.WGSButton))
        self.QueryButton = QPushButton("Query")
        self.QueryButton.clicked.connect(lambda: self.onButtonClicked(self.QueryButton))
        self.BlastButton = QPushButton("Blast")
        self.BlastButton.clicked.connect(lambda: self.onButtonClicked(self.BlastButton))
        self.OutputButton = QPushButton("Output")
        self.OutputButton.clicked.connect(lambda: self.onButtonClicked(self.OutputButton))

        inputGrid = QGridLayout()
        inputGrid.addWidget(self.WGSButton,1,1)
        inputGrid.addWidget(self.QueryButton,1,2)

        self.grid.addLayout(inputGrid,1,1)
        self.grid.addWidget(self.BlastButton, 2, 1)
        self.grid.addWidget(self.OutputButton, 3, 1)

    def onButtonClicked(self, button):
        required = self.getRequired(button.text())
        dialog = OptionDialog(required)
        dialog.exec_()


    def getRequired(self, button):
        flags = [
            { "name" : "Lars", "state" : True},
            { "name" : "Frank", "state" : False},
            { "name" : "Jasper", "state" : False},
            { "name" : "Blast", "state" : False},
            { "name" : "Test", "state" : True},
            { "name" : "Dus...", "state" : False},
        ]
        choices = [
            { "name" : "Type", "options" : ["Nucleotide", "Proteine"]},
            {"name": "Bullshit", "options": ["Nucleotide", "Proteine"]}
        ]
        files = [
            {"type" : "multi"},
            {"type" : "single"}
        ]
        return {"flags" : flags, "choices" : choices, "files" : files}



