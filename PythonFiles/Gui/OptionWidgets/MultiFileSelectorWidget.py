from PyQt5.QtWidgets import *


class MultiFileSelectorWidget(QWidget):
    def __init__(self, filetype=None):
        super().__init__()
        self.files = []
        self.build()
        self.filetype = filetype

    def build(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.listWidget = QListWidget()

        self.openButton = QPushButton("Open")
        self.openButton.clicked.connect(self.onOpen)

        self.grid.addWidget(self.listWidget, 1, 1)
        self.grid.addWidget(self.openButton, 1, 2)

    def onOpen(self):
        names = QFileDialog.getOpenFileNames(self, "Open files", filter=self.filetype)
        for name in names[0]:
            self.files.append(name)
            self.listWidget.addItem(QListWidgetItem(name))

    def result(self):
        return self.files


