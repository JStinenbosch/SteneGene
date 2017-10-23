#!/bin/bash

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/ProteinFiles/Protein/"


output=($(ls | grep ".fa"))
for item in ${output[*]}
do

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"

clustalw -INFILE=ProteinFiles/Protein/${item} -OUTFILE=Clustal/Protein/${item}

done

