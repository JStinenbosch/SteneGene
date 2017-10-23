#!/bin/bash

# This script renames fasta headers

cd "$HOME/Documents/Bovine_S.aureus_sequences//Nucleotide_sequences/BlastOutput/Nucleotide/"
files=($(ls | grep ".fa"))
cd "$HOME/Documents/Bovine_S.aureus_sequences//Nucleotide_sequences/"

if [ ! -d ProteinFiles ]
then 
	mkdir ProteinFiles
fi

if [ ! -d MergeLines/Nucleotide ]
then 
	mkdir MergeLines/Nucleotide
fi


for item in ${files[*]}
do

echo ${item}

perl -0pe 's/(.*)\n(.*)\n/$1 $2\n/g' BedtoolsOutput/${item} > MergeLines/Nucleotide/${item}

	renamed=MergeLines/Nucleotide/${item}

	while read -r first second
	do
		printf "\n>${item}\n" >> ProteinFiles/Nucleotide/${first}.fa
		printf "${second}" >> ProteinFiles/Nucleotide/${first}.fa
				
	done < MergeLines/Nucleotide/${item}
done
