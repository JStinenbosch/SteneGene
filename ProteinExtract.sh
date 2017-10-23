#!/bin/bash


cd "$HOME/Documents/Bovine_S.aureus_sequences//Nucleotide_sequences/BlastOutput/Protein/"
files=($(ls | grep ".fa"))
cd "$HOME/Documents/Bovine_S.aureus_sequences//Nucleotide_sequences/"

for item in ${files[*]}
do

awk '{print $1, $13 }' BlastOutput/Protein/${item} > MergeLines/Protein/${item}

	while read -r first second
	do
		printf "\n>${item}\n" >> ProteinFiles/Protein/${first}.fa
		printf "${second}" >> ProteinFiles/Protein/${first}.fa
				
	done < MergeLines/Protein/${item}
done

