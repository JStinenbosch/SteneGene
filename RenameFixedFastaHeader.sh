#!/bin/bash

# This script renames fasta headers

cd "$HOME/Documents/Bovine_S.aureus_sequences//Nucleotide_sequences/retrieved/"
files=($(ls | grep ".fa"))
cd "$HOME/Documents/Bovine_S.aureus_sequences//Nucleotide_sequences/"

if [ ! -d ProteinFiles ]
then 
	mkdir ProteinFiles
fi

for item in ${files[*]}
do

	paste FixedFiles/QueryHeaders.txt seq.fa > RenamedHeader/${item}

	renamed=RenamedHeader/${item}

	while read -r first second
	do
		echo $second > ProteinFiles/${first}
				
	done < RenamedHeader/Newbould_305.fa
done
