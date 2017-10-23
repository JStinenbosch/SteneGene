from PyQt5.QtWidgets import QPushButton


class InfoButton(QPushButton):
    def __init__(self, required_info, name, *__args):
        super().__init__(name, *__args)
        self.name = name
        self.required = required_info