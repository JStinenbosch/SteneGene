#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we select a file with a
QFileDialog and display its contents
in a QTextEdit.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication, QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon
import sys

from PythonFiles.Gui.PipelineWidget import PipelineWidget


class BlastWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
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