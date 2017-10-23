#!/bin/bash

#translating nucleotide code for all six reading frames (F123R123) in bacterial table (11)

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"

if [ ! -d translations ] 
then 
	#making folder for translations of retrieved nucleotides, named translations
	mkdir translations
	echo "Created directory translations"
fi

#change directory (cd) to the folder with all files
cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/retrieved/"

echo "Grepping nucleotide input file in the current directory"
files=($(ls | grep ".fa"))
for item in ${files[*]}
do

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"

transeq -sequence retrieved/${item} -outseq translations/${item} -frame 6 -table 11
echo "Translated $item"

done
