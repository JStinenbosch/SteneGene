'''
    File name:      Blast.py
    Python Version: 3.5
    Description:    This file is a wrapper around the different BLAST programs.
'''
import os

class Blast(object):

    @staticmethod
    def runBlast():
        return None

    @staticmethod
    def make_blast_db(wgseqs, arguments):
        for WG_Sequence in wgseqs:
            name = os.path.splitext(WG_Sequence)[0]         # Remove file extension
            os.system("makeblastdb -in " + WG_Sequence + " -dbtype nucl -out " + name + "_blastdb")

    @staticmethod
    def blast_query(files, query):
        for WG_Sequence in files:
            print("Blasting for " + WG_Sequence)
            seq_name = os.path.splitext(WG_Sequence)[0]
            query_name = os.path.splitext(query)[0]
            os.system(
                "blastn -query "+  query_name + " -db " + seq_name + "_blastdb -out " + query_name + "_blastout -outfmt 5" +
                " -best_hit_score_edge 0.05 -best_hit_overhang 0.25 -perc_identity 50 -max_target_seqs 1")
