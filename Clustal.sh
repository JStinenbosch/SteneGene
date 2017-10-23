#!/bin/bash

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/MergeLines/Nucleotide/"


output=($(ls | grep ".fa"))
for item in ${output[*]}
do

clustalw -INFILE=MergeLines/Nucleotide/${item} -OUTFILE=Clustal/Nucleotide/${item}

done

