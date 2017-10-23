from PyQt5.QtWidgets import QPushButton


class InfoButton(QPushButton):
    def __init__(self, required_info, *__args):
        super().__init__(*__args)
        self.required = required_info