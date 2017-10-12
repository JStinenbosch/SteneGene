from PyQt5.QtWidgets import *


class MultiFileSelectorWidget(QWidget):
    def __init__(self):
        super().__init__()
        #self.amount = amount
        #self.extensions = extensions

        self.build()

    def build(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.listWidget = QListWidget()

        self.openButton = QPushButton()
        self.openButton.clicked.connect(self.onOpen)

        self.grid.addWidget(self.listWidget, 1, 1)
        self.grid.addWidget(self.openButton, 1, 2)

    def onOpen(self):
        names = QFileDialog.getOpenFileNames(self, "Open files")
        for name in names[0]:
            self.listWidget.addItem(QListWidgetItem(name))


