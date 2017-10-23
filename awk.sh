#!/bin/bash

echo "This script retrieves coordinates of proteins from nucleotide sequences +/- 200 nucleotides"

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"

if [ ! -d bed ] 
then 
	#making folder for databases, named bed
	mkdir bed
	echo "Created directory bed"
fi

cd "output"
echo "changed directory to $path..."

output=($(ls | grep ".fa"))
for item in ${output[*]}
do
cd "$HOME"

echo "Processing $coordinates file..."
#item=`echo "$coordinates" | sed 's/\..*$//g'`
echo "Processing $item file..."
#put variable file names in between the < >
#convert the blasted and sorted file to a range of coordinates for 'bedtools getfasta' by using awk
#and change coordinates from range file to -200 for $6 and +200 for $7 to retrieve a possible start or stop codon outside the matching sequence
perl -lne '/^(.*?)\t.*?\t(\d+)\t(\d+)\t([^\t]*)\t([^\t]*)$/; print "NC_007795.1\t". ($2>$3?$3:$2) . "\t".($2>$3?$2:$3)."\t$1"' /home/jasper/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/output/${item} > /home/jasper/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/bed/${item}
echo "done"

#awk '{print $2,".",".",($5 - 200),($6 + 200),".",".",".","." > "${coordinates}_range"}' $coordinates 

#changing spaces to tabs to make it a .gff file
#awk -v OFS="\t" '$1=$1' $coordinates_range > fcoordinates_range.gff

#extract sequence from nucleotide sequences
#bedtools getfasta -fi RF122.fna_nt -bed RF122_range.gff -fo RF122_nucleotide_list

done

