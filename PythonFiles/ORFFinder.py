'''
    File name:      ORFFinder.py
    Python Version: 3.5
    Description:    This file is a wrapper around the EMBOSS ORF finder.
'''

import os
from Utilities import extract_sequence

class ORFFinder(object):

    @staticmethod
    def ORF_query(query_match):
        print("Finding ORF's for " + query_match)
        name = os.path.splitext(query_match)[0]
        sequence = extract_sequence(name + "_blastout")
        os.system("getorf -sequence " + sequence + " -outseq " + name + "_orfout -minsize 250 -table 11 -find 3")
