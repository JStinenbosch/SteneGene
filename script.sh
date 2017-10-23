#!/bin/bash

echo "This script blasts (tblastn) amino acids to a nucleotides"

FILES=/home/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/db/  #path to folder with all files

for file in $FILES
do
echo "Processing $f file..."

#name=$(basename $f .fsa_nt)

echo $name
echo $f
echo $FILES

tblastn -query /home/jasper/Documents/BLAST/query.txt -db $FILES$name -out $name_output.txt -outfmt "6 qseqid sseqid evalue pident sstart send sseq"

#sort -u -k1,1 --merge $name_output.txt -o $name_output.txt

done



