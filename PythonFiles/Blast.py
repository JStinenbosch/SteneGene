'''
    File name:      Blast.py
    Python Version: 3.5
    Description:    This file is a wrapper around the different BLAST programs.
'''

import os
from Utilities import add_property_to_string

class Blast(object):

    @staticmethod
    def runBlast():
        pass

    @staticmethod
    def make_blast_db(wgseqs, arguments):
        arg_string = ""
        arg_string = add_property_to_string("dbtype", arguments, arg_string, "nucl")

        for WG_Sequence in wgseqs:
            name = os.path.splitext(WG_Sequence)[0]         # Remove file extension
            os.system("makeblastdb -in " + WG_Sequence + " -out " + name + "_blastdb " + arg_string)

    @staticmethod
    def blast_query(wgseqs, query_paths, output_path, arguments, query_flag, seq_flag):
        """ This function handles calls to the BLAST programs. Documentation from:
            https://www.ncbi.nlm.nih.gov/books/NBK279675/
        """
        arg_string = ""
        # Best Hit algorithm score edge value (recommended value: 0.1)
        arg_string = add_property_to_string("best_hit_score_edge", arguments, arg_string, "0.1")
        # Best Hit algorithm overhang value (recommended value: 0.1)
        arg_string = add_property_to_string("best_hit_overhang", arguments, arg_string, "0.1")
        # Percent identity cutoff.
        arg_string = add_property_to_string("perc_identity", arguments, arg_string, "0")
        # Length of initial exact match.
        arg_string = add_property_to_string("word_size", arguments, arg_string, "11")
        print("Printing " + ascii(arg_string))
        blast_xml_path = []

        for WG_Sequence in wgseqs:
            for query in query_paths:
                print("Blasting for " + WG_Sequence)
                seq_name = os.path.splitext(WG_Sequence)[0]
                exec_string = ""
                if seq_flag['dbtype'] == "nucl":
                    if query_flag['seq_type'] == "nucl":
                        exec_string = "blastn"
                    else:
                        exec_string = "tblastn"
                elif seq_flag['dbtype'] == "prot":
                    if query_flag['seq_type'] == "nucl":
                        exec_string = "blastx"
                    else:
                        exec_string = "blastp"
                os.system(
                    exec_string + " -query " + query + " -db " + seq_name + "_blastdb -out " + output_path + "_" +
                    os.path.splitext(os.path.basename(WG_Sequence))[0] + ".xml -outfmt 5 " + arg_string)

            blast_xml_path.append(output_path + "_" + os.path.splitext(os.path.basename(WG_Sequence))[0] + ".xml")

        return blast_xml_path

