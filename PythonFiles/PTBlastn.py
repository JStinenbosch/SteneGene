'''
    File name:      PTBlastn.py
    Authors:        JStinenbosch and FrankTN
    Python Version: 3.5
    Description:    This file contains the functions used in the Blast analysis. This script should be run with a list
                    of fasta files on its input.
'''

import os
import sys
import argparse
from Utilities import *
from Bio.Blast import NCBIXML

acceptable_extensions = ['.fasta', '.fas', '.fa', '.fsa', '.fna', '.fsa_nt']
CURRENT_DIR = os.getcwd()

# THIS PART WILL BE REPLACED BY GUI
def readInput():
    parser = argparse.ArgumentParser(description='Match query files to WGS input')
    parser.add_argument('wgs', metavar='wgs_files', type=str, nargs='+',
                        help='List containing at least one WGS file')
    parser.add_argument("query",type=str,nargs='+', help='List containing the queries')
    return parser.parse_args()

# Auxiliary functions

def make_blast_db(files):
    for WG_Sequence in files:
        name = os.path.splitext(WG_Sequence)[0]
        os.system("makeblastdb -in " + WG_Sequence + " -dbtype nucl -out " + name + "_blastdb")

def blast_query(files):
    for WG_Sequence in files:
        print("Blasting for " + WG_Sequence)
        name = os.path.splitext(WG_Sequence)[0]
        os.system(
            "blastn -query GeneQuery.fa -db " + name + "_blastdb -out " + name + "_blastout -outfmt 5" +
            " -best_hit_score_edge 0.05 -best_hit_overhang 0.25 -perc_identity 50 -max_target_seqs 1")

def ORFfinder(query_matches):
    for candidate in query_matches:
        print ("Finding ORF's for " + candidate)
        name = os.path.splitext(candidate)[0]
        os.system("getorf -sequence " + name + "_blastout -outseq " + name + "_orfout -minsize 250 -table 11 -find 3")

def check_extensions(files):
    wgs_files = list(filter(lambda name: name.endswith(tuple(acceptable_extensions)), files))
    if not wgs_files:
        print("Incorrect extension, we only allow " + str(acceptable_extensions))
        exit(-1)
    return wgs_files

# Start of script

print("\nThis script blasts proteins to nucleotides (blastn)\n\n")
print('''Getting in folder 'Nucleotide_sequences' all files with the following extensions:
    .fasta, .fas, .fa, .seq, .fsa: Generic FASTA
    .fna, .fna_nt, .fsa_nt: FASTA nucleic acids\n
    But not the following extentions:
    .ffn: FASTA nucleotide coding regions for a genome
    .faa FASTA amino acids
    .mpfa: FASTA amino acides in multiple proteins
    .frn: FASTA non-coding RNA
    .fastq: FASTQ\n\n''')

arguments = readInput()
wgs_files = check_extensions(arguments.wgs)
query_list = check_extensions(arguments.query)

query = handle_input_files(query_list)

make_blast_db(wgs_files)
print(wgs_files)
os.system("cd BlastDB && echo $PWD && echo databases have been produced")
blast_query(wgs_files)
ORFfinder(wgs_files)