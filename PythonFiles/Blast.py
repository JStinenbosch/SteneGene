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
        arg_list = []
        add_property_to_string("dbtype", arguments, arg_list, "nucl")
        arg_string = "".join(arg_list)

        for WG_Sequence in wgseqs:
            name = os.path.splitext(WG_Sequence)[0]         # Remove file extension
            os.system("makeblastdb -in " + WG_Sequence + " -out " + name + "_blastdb " + arg_string)

    @staticmethod
    def blast_query(files, query, arguments):
        """ This function handles calls to the BLAST programs. Documentation from:
            https://www.ncbi.nlm.nih.gov/books/NBK279675/
        """
        arg_list = []
        # Best Hit algorithm score edge value (recommended value: 0.1)
        add_property_to_string("best_hit_score_edge", arguments, arg_list, "0.1")
        # Best Hit algorithm overhang value (recommended value: 0.1)
        add_property_to_string("best_hit_overhang", arguments, arg_list, "0.1")
        # Percent identity cutoff.
        add_property_to_string("perc_identity", arguments, arg_list, "0")
        # Length of initial exact match.
        add_property_to_string("word_size", arguments, arg_list, "11")

        arg_string = "".join(arg_list)
        print("Printing " + ascii(arg_string))

        for WG_Sequence in files:
            print("Blasting for " + WG_Sequence)
            seq_name = os.path.splitext(WG_Sequence)[0]
            query_name = os.path.splitext(query)[0]
            os.system(
                "blastn -query " +  query + " -db " + seq_name + "_blastdb -out " + query_name + "_blastout -outfmt 5 "
                + arg_string)


