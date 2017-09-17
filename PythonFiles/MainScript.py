'''
    File name:      PTBlastn.py
    Python Version: 3.5
    Description:    This file contains the functions used in the Blast analysis. This script should be run with a list
                    of fasta files on its input.
'''

import argparse
from Utilities import *
from Blast import *
from ORFFinder import *

def readInput():
    parser = argparse.ArgumentParser(description='Match query files to WGS input')
    parser.add_argument('wgs', metavar='wgs_files', type=str, nargs='+',
                        help='List containing at least one WGS file')
    parser.add_argument("query",type=str,nargs='+', help='List containing the queries')
    return parser.parse_args()

# Start of script

print("\nThis script blasts proteins to nucleotides (blastn)\n\n")
print('''Getting in folder 'Nucleotide_sequences' all files with the following extensions:
    .fasta, .fas, .fa, .seq, .fsa: Generic FASTA
    .fna, .fna_nt, .fsa_nt: FASTA nucleic acids\n
    But not the following extensions:
    .ffn: FASTA nucleotide coding regions for a genome
    .faa FASTA amino acids
    .mpfa: FASTA amino acides in multiple proteins
    .frn: FASTA non-coding RNA
    .fastq: FASTQ\n\n''')

arguments = readInput()
wgs_files = check_extensions(arguments.wgs)
query_list = check_extensions(arguments.query)

query_filename = handle_input_files(query_list)

Blast.make_blast_db(wgs_files, {"example": "value"})
os.system("cd BlastDB && echo $PWD && echo databases have been produced")
Blast.blast_query(wgs_files, query_filename)
ORFFinder.ORF_query(query_filename)