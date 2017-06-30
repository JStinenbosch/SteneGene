#!/bin/bash

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"

if [ ! -d MergedProteinList ] 
then 
	mkdir MergedProteinList
	echo "Created directory MergedProteinList"
fi

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/ProteinFiles/"
files=($(ls | grep "CLFA\|CLFB\|EBPS\|FNBA\|ISAA\|ISDA\|ISDB"))

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/ProteinFiles/"
#for name in ${files[*]}
#do

#cat ProteinFiles/${name} > MergedProteinList/out
ls | grep "CLFA\|CLFB\|EBPS\|FNBA\|ISAA\|ISDA\|ISDB" | while read file; do cat $file >> output.txt; done;

#done

