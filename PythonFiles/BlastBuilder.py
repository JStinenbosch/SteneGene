from PythonFiles import BlastParser
from PythonFiles.Blast import Blast




class BlastBuilder(object):

    def __init__(self):
        self.blast_query = []
        self.WGS_flags = {}
        self.WGS_paths = []

        self.query_flags = {}

        self.blast_parameters = {}

    def set_WGS_paths(self, path_list: list):
        self.WGS_paths = path_list

    def set_WGS_flags(self, seq_type: str):
        if seq_type in ["Nucleotide", "N"]:
            self.WGS_flags['dbtype'] = "nucl"
        else:
            self.WGS_flags['dbtype'] = "prot"

    def set_query_paths(self, path_list: list):
        self.query_paths = path_list

    def set_query_flags(self, seq_type: str):
        if seq_type in ["Nucleotide", "N"]:
            self.query_flags['seq_type'] = "nucl"
        else:
            self.query_flags['seq_type'] = "prot"

    def set_blast_param(self, parameter_dict: dict):
        self.blast_parameters = parameter_dict

    def set_output_file(self, target_output: str):
        self.output_path = target_output

    def is_runnable(self):
        #Checks whether WGS_paths and query_paths
        return hasattr(self, "WGS_paths") and hasattr(self, "query_paths") and hasattr(self, "output_path")

    def run_blast(self):
        Blast.make_blast_db(self.WGS_paths, self.WGS_flags)
        self.blast_xml = Blast.blast_query(self.WGS_paths, self.query_paths, self.output_path, self.blast_parameters, self.query_flags, self.WGS_flags)

    def parse_blast(self):
        BlastParser.add_dir_to_path(self.blast_xml)
        BlastParser.xml_to_fasta_files(self.blast_xml, expect_value=0.01)
