#!/bin/bash

echo "This script retrieves coordinates of proteins from nucleotide sequences +/- 200 nucleotides"

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"

if [ ! -d bed ] 
then 
	#making folder for bedfiles, named bed
	mkdir bed
	echo "Created directory bed"
fi

if [ ! -d bed2 ] 
then 
	#making folder for bedfiles, named bed
	mkdir bed2
	echo "Created directory bed"
fi

cd "BlastOutput/Nucleotide/"
echo "changed directory to $path..."

output=($(ls | grep ".fa"))
for item in ${output[*]}
do

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"

#converting blast output (outfmt 6) to bed format
echo "Processing $item..."


perl -lne '/^(.*?)\t.*?\t(\d+)\t(\d+)\t([^\t]*)\t([^\t]*)$/; print "chr\t". ($2>$3?$3:$2) . "\t".($2>$3?$2:$3)."\t$1"' BlastOutput/Nucleotide/${item} > bed/${item}



#awk '{ print $2-200, $3+200 > "bed2/${item}" }' bed/${item} 


done

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/bed"

for file in *.fa; do
    mv "$file" "`basename "$file" .fa`.bed"
	echo "Replacing extention from .fa > .bed for $file..."

done

