#!/bin/bash

cd "$HOME/Documents/Bovine_S.aureus_sequences//Nucleotide_sequences/ProteinFiles/"
files=($(ls | grep ".out"))
cd "$HOME/Documents/Bovine_S.aureus_sequences//Nucleotide_sequences/"

for item in ${files[*]}
do

mv ProteinFiles/${item} Clustal/${item}

done
