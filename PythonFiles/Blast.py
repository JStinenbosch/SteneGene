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
        if "dbtype" in arguments:
            type = arguments["dbtype"]
        else:
            type = "nucl"

        for WG_Sequence in wgseqs:
            name = os.path.splitext(WG_Sequence)[0]         # Remove file extension
            os.system("makeblastdb -in " + WG_Sequence + " -dbtype " + type + " -out " + name + "_blastdb")

    @staticmethod
    def blast_query(files, query, arguments):
        if "word_size" in arguments:
            word_size = arguments["word_size"]
        else:
            word_size = "11"

        if "best_hit_score_edge" in arguments:
            best_hit = arguments["best_hit_score_edge"]
        else:
            best_hit = "0.1"

        if "best_hit_overhang" in arguments:
            best_overhang = arguments["best_hit_overhang"]
        else:
            best_overhang = "0.1"

        if "perc_identity" in arguments:
            perc_identity = arguments["perc_identity"]
        else:
            perc_identity = "0"

        for WG_Sequence in files:
            print("Blasting for " + WG_Sequence)
            seq_name = os.path.splitext(WG_Sequence)[0]
            query_name = os.path.splitext(query)[0]
            os.system(
                "blastn -query "+  query + " -db " + seq_name + "_blastdb -out " + query_name + "_blastout -outfmt 5" +
                " -best_hit_score_edge " + best_hit + " -best_hit_overhang " + best_overhang +
                " -perc_identity " + perc_identity + " -max_target_seqs 1 -word_size " + word_size)
