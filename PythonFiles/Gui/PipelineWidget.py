from PyQt5.QtWidgets import *

from Gui.CustomButtons import InfoButton
from PythonFiles.Gui.OptionDialog import OptionDialog


class PipelineWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.WGSButton = InfoButton([
            {"type": "multi_file", "id": "2", "info": {}},
            {"type": "choice", "id": "1", "info": {"label": "Type", "options": ["Nucleotide", "Protein"]}}
        ], "WGS")
        self.WGSButton.clicked.connect(lambda: self.onButtonClicked(self.WGSButton))
        self.QueryButton = InfoButton([
            {"type": "multi_file", "id": "2", "info": {}},
            {"type": "choice", "id": "1", "info": {"label": "Type", "options": ["Nucleotide", "Protein"]}}
        ], "Query")
        self.QueryButton.clicked.connect(lambda: self.onButtonClicked(self.QueryButton))
        self.BlastButton = InfoButton([
            {"type": "text_edit", "id": "1", "info": {"label": "best_hit_score_edge", "default": "0.1"}},
            {"type": "text_edit", "id": "2", "info": {"label": "best_hit_overhang", "default": "0.1"}},
            {"type": "text_edit", "id": "3", "info": {"label": "perc_identity", "default": "0"}},
            {"type": "text_edit", "id": "4", "info": {"label": "word_size", "default": "11"}},

        ], "Blast")
        self.BlastButton.clicked.connect(lambda: self.onButtonClicked(self.BlastButton))
        self.OutputButton = InfoButton([
            {"type": "single_file", "id": "1", "info": {}}
        ], "Output")
        self.OutputButton.clicked.connect(lambda: self.onButtonClicked(self.OutputButton))

        inputGrid = QGridLayout()
        inputGrid.addWidget(self.WGSButton, 1, 1)
        inputGrid.addWidget(self.QueryButton, 1, 2)

        self.grid.addLayout(inputGrid, 1, 1)
        self.grid.addWidget(self.BlastButton, 2, 1)
        self.grid.addWidget(self.OutputButton, 3, 1)

        ok_button = QPushButton("&Run")
        ok_button.clicked.connect(self.accept)
        self.grid.addWidget(ok_button, 4, 1)

    def accept(self):
        if self.controller.can_run():
            self.controller.run_blast()
            self.controller.parse_blast()
        return

    def onButtonClicked(self, button):
        required = button.required
        name = button.name
        dialog = OptionDialog(name, required)
        if dialog.exec_():
            results = dialog.result()
            self.updateController(results, button)

    def updateController(self, results, button):
        if button.name == "WGS":
            dict = {"WGS_path": results["2"], "seq_type": results["1"]}
            self.controller.set_WGS(dict)
        elif button.name == "Query":
            dict = {"query_path": results["2"], "seq_type": results["1"]}
            self.controller.set_query(dict)
        elif button.name == "Blast":
            blast_dict = {}
            for k in results:
                blast_dict[results[k]["label"]] = results[k]["value"]
            self.controller.set_blast_param(blast_dict)
        elif button.name == "Output":
            self.controller.set_output_file(results['1'])
            print("Output")
