#!/bin/bash

#This script finds and extract open reading frames (ORF)

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences"

if [ ! -d orf ] 
then 
	#making folder for orfs, named orf
	mkdir orf
	echo "Created directory orf"
fi

#cd to right directory for translated sequences
cd  "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/BedtoolsOutput"

echo "Grepping database input file in the current directory"
files=($(ls | grep ".fa"))
for item in ${files[*]}
do
echo "$item"

cd  "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"

getorf -sequence BedtoolsOutput/${item} -outseq orf/${item}  -minsize 300 -table 11

echo "Reading frames retrieved"

done
