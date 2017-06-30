#!/bin/bash

# This script renames fasta headers

cd "$HOME/Documents/Bovine_S.aureus_sequences/Test/"

# fetch every alternate line (i.e. the sequences) and put them in a temporary file, from bedtools output file

awk 'NR%2==0' RF122.fa > seq.fa

# fetch protein names for fasta headers, from blast output file

awk '{print ">"$1 > "Headers.txt"}' RF122.fna_nt_out.txt

# insert a line with headers from the header text file for every sequence line

paste -d'\n' Headers.txt seq.fa > RF122_Headers.fa
