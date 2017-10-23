#!/bin/bash

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/ProteinFiles/Nucleotide/"


output=($(ls | grep ".fa"))
for item in ${output[*]}
do

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"

clustalw -INFILE=ProteinFiles/Nucleotide/${item} -OUTFILE=Clustal/Nucleotide/${item}

done

