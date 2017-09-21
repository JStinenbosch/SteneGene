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
        if "dbtype" in arguments:
            type = arguments["dbtype"]
        else:
            type = "nucl"

        for WG_Sequence in wgseqs:
            name = os.path.splitext(WG_Sequence)[0]         # Remove file extension
            os.system("makeblastdb -in " + WG_Sequence + " -dbtype " + type + " -out " + name + "_blastdb")

    @staticmethod
    def blast_query(files, query, arguments):
        arg_string = ""
        arg_string = add_property_to_string("best_hit_score_edge", arguments, arg_string, "0.1")
        arg_string = add_property_to_string("best_hit_overhang", arguments, arg_string, "0.1")
        arg_string = add_property_to_string("perc_identity", arguments, arg_string, "0")
        arg_string = add_property_to_string("word_size", arguments, arg_string, "11")
        print("Printing " + ascii(arg_string))

        for WG_Sequence in files:
            print("Blasting for " + WG_Sequence)
            seq_name = os.path.splitext(WG_Sequence)[0]
            query_name = os.path.splitext(query)[0]
            os.system(
                "blastn -query " +  query + " -db " + seq_name + "_blastdb -out " + query_name + "_blastout -outfmt 5 "
                + arg_string)


