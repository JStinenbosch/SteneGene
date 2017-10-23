from PyQt5.QtWidgets import *


class SingleFileSelectorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.files = []
        self.build()

    def build(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.label = QLabel("...")
        self.label.setFixedWidth(100)

        self.openButton = QPushButton("Select output")
        self.openButton.clicked.connect(self.onOpen)

        self.grid.addWidget(self.label, 1, 1)
        self.grid.addWidget(self.openButton, 1, 2)

    def onOpen(self):
        name = QFileDialog.getSaveFileName(self, "Output")
        self.file = name[0]
        self.label.setText(name[0])

    def result(self):
        return self.file


