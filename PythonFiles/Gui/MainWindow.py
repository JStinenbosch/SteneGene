#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This file contains the main window for the Blast helper. This window displays some buttons linking to dynamically
generated dialogs to create a blast query.
"""

from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication, QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon
import sys

from PythonFiles.Gui.PipelineWidget import PipelineWidget


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.setWindowTitle("Blast Helper")
        self.setFixedSize(self.sizeHint())
        self.controller = controller

    def initUI(self):
        self.pipeline = PipelineWidget()
        self.setCentralWidget(self.pipeline)
        self.show()

    def run(self):
        self.initUI()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BlastWindow("test")
    ex.run()
    sys.exit(app.exec_())