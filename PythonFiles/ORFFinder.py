"""
    File name:      ORFFinder.py
    Python Version: 3.5
    Description:    This file is a wrapper around the EMBOSS ORF finder.
"""

import os
from Utilities import extract_sequence, add_property_to_string


class ORFFinder(object):

    @staticmethod
    def ORF_query(query_name: str, arguments: dict = {}) -> None:
        """
            This function runs the getorf command on the system after first parsing the argument dict.
            Documentation was obtained from http://emboss.sourceforge.net/apps/cvs/emboss/apps/getorf.html
        """
        arg_string = ""
        # The minimum size of the ORF to report, defaults to 250 nucleotides
        arg_string = add_property_to_string("minsize", arguments, arg_string, "250")
        # The type of table to use for the initiation codons. Default type 1, which uses alternative initiation codons
        arg_string = add_property_to_string("table", arguments, arg_string, "1")
        # The type of output to be produced. The default of 3 gives the sequence of nucleotides between the START and
        # STOP codons.
        arg_string = add_property_to_string("find", arguments, arg_string, "3")

        extensionless_name = os.path.splitext(query_name)[0]
        os.system("getorf -sequence " + query_name + " -outseq " + extensionless_name + "_orfout " + arg_string)
