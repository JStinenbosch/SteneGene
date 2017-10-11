"""
    File name:      ClustalOmega.py
    Python Version: 3.5
    Description:    This file is a wrapper around the EMBL-EBI multiple sequence alignment program Clustal Omega .
"""

import os
from Utilities import extract_sequence, add_property_to_string


class ClustalOmega(object):/5

    @staticmethod
    def clustalo(gene_list, arguments):

        arg_string = ""
        arg_string = add_property_to_string("-outfmt=", arguments, arg_string, "0.1")



#    clustalo -i ProteinFiles/${fastaSeq} -obClustal/${fastaSeq} --outfmt=clustal -v --dealign --force

        extensionless_name = os.path.splitext(query_name)[0]
os.system("clustalo -i " + gene_list + " -o " + gene + "_clustal " + arg_string)