'''
    File name:      PTBlastn.py
    Authors:        JStinenbosch and FrankTN
    Python Version: 3.5
    Description:    This file contains the functions used in the Blast analysis. This script should be run with a list
                    of fasta files on its input.
'''

import os
import sys
from Utilities import *

acceptable_extensions = ['.fasta', '.fas', '.fa', '.fsa', '.fna', '.fsa_nt']
CURRENT_DIR = os.getcwd()


# THIS PART WILL BE REPLACED BY GUI
def readInput():
    if len(sys.argv) < 2:
        print("Please specify input file")
        exit(-1)

    return sys.argv[1:]


# THIS PART WILL BE REPLACED BY GUI

def make_blast_db(files):
    os.makedirs("BlastDB",exist_ok=True)
    for sequence in files:
        os.system("makeblastdb -in " + sequence + " -dbtype nucl -out BlastDB/" + sequence)

def blast_query(files):
    os.makedirs("BlastOutput",exist_ok=True)
    for f in files:
        print("Blasting for " + f)
        os.system(
            "blastn -query ProteinQuery.fa -db BlastDB/" + f + " -out BlastOutput/" + f + " -outfmt 5" +
            " -best_hit_score_edge 0.05 -best_hit_overhang 0.25 -perc_identity 50 -max_target_seqs 1")

def ORFfinder(files):
    os.makedirs("ORF_out",exist_ok=True)
    for f in files:
        print ("Finding ORF's for " + f)
        os.system("getorf -sequence BlastOutput/" + f + " -outseq ORF_out/" + f + " -minsize 250 -table 11 -find 3")

# Start of script


print("\nThis script blasts proteins to nucleotides (blastn)\n\n")
print('''Getting in folder 'nucleotide_sequences' all files with the following extensions:
    .fasta, .fas, .fa, .seq, .fsa: Generic FASTA
    .fna, .fna_nt, .fsa_nt: FASTA nucleic acids\n
    But not the following extentions:
    .ffn: FASTA nucleotide coding regions for a genome
    .faa FASTA amino acids
    .mpfa: FASTA amino acides in multiple proteins
    .frn: FASTA non-coding RNA
    .fastq: FASTQ\n\n''')

if not os.path.exists(CURRENT_DIR + "/Nucleotide_sequences/"):
    print("Creating local directory /Nucleotide_sequences/")
    os.makedirs(CURRENT_DIR + "/Nucleotide_sequences/", exist_ok=True)
    print("Please add your nucleotide sequences to this directory")
    exit(-1)

files = readInput()
for name in files:
    if not name.endswith(tuple(acceptable_extensions)):
        print("Incorrect extension, we only allow " + str(acceptable_extensions))
        exit(-1)

query = handle_input_files(files)

make_blast_db(files)
print(files)
os.system("cd BlastDB && echo $PWD && echo databases have been produced")
blast_query(files)
ORFfinder(files)

make_blast_db(files)
print(files)
os.system("cd BlastDB && echo $PWD && echo databases have been produced")
blast_query(files)