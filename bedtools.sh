#!/bin/bash

#This script retrieves nucleotide sequences from the genome for coordinates

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"

if [ ! -d BedtoolsOutput ] 
then 
	#making folder for bedfiles, named BedtoolsOutput
	mkdir BedtoolsOutput
	echo "Created directory BedtoolsOutput"
fi

# Removing all .fai files for next run
ls | grep ".fai" | xargs rm 

#grepping files for bedtools getfasta
	#input: -fi, nucleotide sequences, <name>.fsa_nt
	#range: -bed, ranges from bed
	#output: -fo, directed to retrieved/ , same filename in <name>.bed format
										 # removed $fi extention to procude the bed file
	
echo "Grepping database input file in the current directory"
files=($(ls | grep ".fsa_nt\|.fna_nt"))
echo "$files"
cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"

for fi in ${files[*]}
do
echo "$fi"

#Removing extentions of $fi to get the bed file, called item
item=`echo $fi | sed -e 's/\.[^.]*$//'`
echo "$item"
#extract sequence from nucleotide sequences
bedtools getfasta -fi ${fi} -bed bed/${item}.bed -fo BedtoolsOutput/${fi} -name
echo "done"
done

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/BedtoolsOutput/"
  
  	for file in *.fsa_nt
	do
	mv "$file" "${file%.fsa_nt}.fa"
	done
