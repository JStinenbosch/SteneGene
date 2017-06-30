#!/bin/bash

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/output/"

for file in *.fsa_nt_out.txt\|*.fna_nt_out.txt
do
 mv "$file" "${file%.fsa_nt_out.txt\|file%.fna_nt_out.txt}.fa"
done
