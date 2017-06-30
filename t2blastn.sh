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

if [ ! -d BlastOutput ]
then
	#making folder for result outputs, named BlastOutput
	echo "Created directory BlastOutput"
	mkdir BlastOutput
fi

#getting in folder nucleotide_sequences all files with the extention fsa_nt or fna_nt
nucleotide_sequences=($(ls | grep ".fsa_nt\|.fna_nt"))
for sequence in ${nucleotide_sequences[*]}
do
	makeblastdb -in $sequence -dbtype nucl -out /home/jasper/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/db/$sequence
done

echo "all databases produced" 

#change directory (cd) to the folder with all files
cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/db/"

echo "changed directory to: $PWD"

#list all files in the folder, just to check!
printf "List of all files in this directory:\n"
ls

echo "Grepping database input file in the current directory"
files=($(ls | grep ".fsa_nt.nsq\|.fna_nt.nsq"))
for name in ${files[*]}
do
  cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"
  echo "changed directory to: $PWD"
  #removing the .nsq extension in some weird manner because the blast cannot read extentions after the fsa_nt
  item=`echo ${name} | sed -e 's/\.[^.]*$//'`
  printf "removed extension to make file format suitable for blast for $item\n"
  printf "blasting ...\n"  
  tblastn -query FixedFiles/ProteinQuery.fa -db db/${item} -max_hsps 1 -out BlastOutput/${item} -outfmt "6 evalue qseqid sseqid pident length mismatch gapopen qstart qend sstart send bitscore sseq"
  echo "Sorting output to produce one hit per protein for $item"
  #sort -u -k1,1 --merge $HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/BlastOutput/${item} -o $HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/BlastOutput/${item}
  
cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/BlastOutput/"
  
  	for file in *.fsa_nt
	do
	mv "$file" "${file%.fsa_nt}.fa"
	done

echo "All files converted"

done 
