#!/bin/bash



#change directory (cd) to the folder with all files
cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/db/"



echo "Grepping database input file in the current directory"
files=($(ls | grep ".fsa_nt.nsq\|.fna_nt.nsq"))
for name in ${files[*]}
do
  #removing the .nsq extension in some weird manner because the blast cannot read extentions after the fsa_nt
  item=`echo $name | sed -e 's/\.[^.]*$//'`
  printf "removed extension to make file format suitable for blast for $item\n"
  printf "blasting ...\n"
  tblastn -query /home/jasper/Documents/BLAST/query.txt -db /home/jasper/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/db/${item} -out /home/jasper/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/output/${item}_out.txt -outfmt 6
  echo "Sorting output to produce one hit per protein for $item"
  sort -u -k1,1 --merge $HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/output/${item}_out.txt -o $HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/output/${item}_out.txt
  printf "stored output as: ${item}_out.txt\n"
done

echo "All files converted"

