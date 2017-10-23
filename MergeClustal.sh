#!/bin/bash


cd "$HOME/Documents/Bovine_S.aureus_sequences//Nucleotide_sequences/Clustal/Nucleotide/"
files=($(ls | grep ".fa"))

cd "$HOME/Documents/Bovine_S.aureus_sequences//Nucleotide_sequences/Clustal/Protein/"
docs=($(ls | grep ".fa"))

cd "$HOME/Documents/Bovine_S.aureus_sequences//Nucleotide_sequences/Clustal/"

for item in ${files[*]}, name in ${docs[*]}
do
		printf "${name}\n" > Merge/${name}
		paste -d"\n" Protein/${name} Nucleotide/${item} >> Merge/${name}
		
done
