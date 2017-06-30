#!/bin/bash

printf "This script blasts proteins to nucleotides (tblastn)\n"
if [ ! -d "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/" ] 
then 
	#making folder for databases, named db
	echo "Created directory Bovine_S.aureus_sequences/Nucleotide_sequences/"
	mkdir "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"
	echo "Please add your nucleotide sequences to this directory"
	exit
fi
cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"
if [ ! -d db ] 
then 
	#making folder for databases, named db
	echo "Created directory db"
	mkdir db
fi
if [ ! -d output ]
then
#making folder for result outputs, named output
	echo "Created directory output"
	mkdir output
fi
nucleotide_sequences=($(ls | grep ".fsa_nt"))
for sequence in ${nucleotide_sequences[*]}
do
	makeblastdb -in $sequence -dbtype nucl -out /home/jasper/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/db/$sequence 
done

echo "all databases produced" 

#change directory (cd) to the folder with all files
cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/db/"

echo "changed directory to: $path"

#list all files in the folder, just to check! :P
printf "List of all files in this directory:\n"
ls

echo "Grepping database input file in the current directory"
files=($(ls | grep ".fsa_nt.nsq"))
for name in ${files[*]}
do
  item=`echo $name | sed -e 's/\.[^.]*$//'`
  printf "removed extension to make file format suitable for blast for $item\n"
  printf "blasting ...\n"
  printf "hacking NASA\n"
  printf "blasting again ...\n"
  tblastn -query /home/jasper/Documents/BLAST/query.txt -db /home/jasper/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/db/${item} -out /home/jasper/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/output/${item}_out.txt -outfmt "6 qseqid sseqid evalue pident sstart send sseq"
  echo "Sorting output to produce one hit per protein for $item"
  sort -u -k1,1 --merge $HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/output/${item}_out.txt -o $HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/output/${item}_out.txt
  printf "stored output as: ${item}_out.txt\n"
done

echo "All files converted"

