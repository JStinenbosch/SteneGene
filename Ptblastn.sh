#!/bin/bash

printf "\nThis script blasts proteins to nucleotides (tblastn)\n\n"
printf " Getting in folder 'nucleotide_sequences' all files with the following extensions:
    .fasta, .fas, .fa, .seq, .fsa: Generic FASTA
    .fna, .fna_nt, .fsa_nt: FASTA nucleic acids\n
 But not the following extentions:
    .ffn: FASTA nucleotide coding regions for a genome
    .faa FASTA amino acids
    .mpfa: FASTA amino acides in multiple proteins
    .frn: FASTA non-coding RNA
    .fastq: FASTQ\n\n"

# If directory .../Nucleotide_sequences/ does not exist we make it and exit
if [ ! -d "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/" ]
then
	echo "Created directory Bovine_S.aureus_sequences/Nucleotide_sequences/"
	mkdir "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"
	echo "Please add your nucleotide sequences to this directory"
	exit
fi

# Move control into the nucleotide sequences folder
cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/"
# If the Protein/ directory exists, we remove all the files inside
if [ -d "Protein/" ]
then
	echo "Removing old files in directory Protein..."
	rm -rf Protein/
    echo "Done"
fi

# We make the Protein/ folder and move into it
mkdir Protein
echo "Created directory Protein/"
cd "Protein/"

# Making folder for databases, named BlastDB
mkdir BlastDB/
echo "Created directory BlastDB/"

# Making folder for result outputs, named BlastOutput
mkdir BlastOutput/
echo "Created directory BlastOutput/"

mkdir MergeLines/
echo "Created directory MergeLines/"

mkdir ProteinFiles/
echo "Created directory ProteinFiles/"

mkdir Clustal/
echo "Created directory Clustal/"

mkdir Temp/
echo "Created directory Temp/"

# Change directory back two folders to find the query proteins
cd ../..

# Read every separate protein file (with the correct extension) and paste them into one file
# Files send to 1>
# Errors of cat for missing extensions send to 2> (empty folder) to prevent unnecessary errors in prompt
cat Query/Proteins/*.{fsa_nt,fa,fsa,fas,seq,fasta,fna_nt,fna} 1>Nucleotide_sequences/Protein/Temp/ProteinQuery.fa 2>/dev/null

# Change directory back to the working folder
cd Nucleotide_sequences/

# Copy ProteinQuery file and rename as QueryTemp for further use
cp Protein/Temp/ProteinQuery.fa Protein/Temp/QueryTemp.fa

awk '/^>/{print s? s"\n"$0:$0;s="";next}{s=s sprintf("%s",$0)}END{if(s)print s}' Protein/Temp/QueryTemp.fa > Protein/Temp/QueryTemp2.fa

awk 'NR%2{printf "%s ",$0;next;}1' Protein/Temp/QueryTemp2.fa > Protein/Temp/QueryTemp3.fa

#Remove the ">" character in front of every protein line (originated from the fasta format)
sed 's/^.\{1\}//' Protein/Temp/QueryTemp3.fa > Protein/MergeLines/Query.fa

nucleotide_sequences=($(ls | grep ".fsa_nt\|.fa\|.fsa\|.fas\|.seq\|.fasta\|.fna_nt\|.fna"))

for sequence in ${nucleotide_sequences[*]}
do
	makeblastdb -in ${sequence} -dbtype nucl -out Protein/BlastDB/${sequence}
done

echo "all databases produced" 

#change directory (cd) to the folder with all files
cd "Protein/BlastDB/"

echo "changed directory to: $PWD"

#list all files in the folder, just to check!
printf "List of all files in this directory:\n"
ls

echo "Grepping database input file in the current directory"
files=($(ls | grep ".fsa_nt.nsq\|.fna_nt.nsq"))
for name in ${files[*]}
do

  cd ../..

  # Removing the .nsq extension in some weird manner because the blast cannot read extentions after the fsa_nt
  item=`echo ${name} | sed -e 's/\.[^.]*$//'`

  printf "blasting for ${item} ...\n"
  # Use -max_hsps 1 to obtain only one output
  tblastn -query FixedFiles/ProteinQuery.fa -db Protein/BlastDB/${item} -out Protein/BlastOutput/${item} -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore sseq"

  # Removing sequences with more than 50 mismatches. The E value is good, but it favours long sequences even though there are a lot of
  # mismatches. So removing lines with more than 50 mismatches fixes this problem.
  awk '(NR==1) || ($5 < 100 )' Protein/BlastOutput/${item} > Protein/BlastOutput/${item}.2

  # Sorting output to produce one hit per protein for $item
  sort -u -k1,1 --merge Protein/BlastOutput/${item}.2 -o Protein/BlastOutput/${item}.3

  # Removing sequences with less then 30 percent similarity, these usually are not the same protein and also not fragments of the protein.
  awk '(NR==1) || ($3 > 30 )' Protein/BlastOutput/${item}.3 > Protein/BlastOutput/${item}.4


    #Changing the extention of the files from .fsa_nt.4 to .fa
    cd Protein/BlastOutput/

  	for file in *.fsa_nt.4
	do
	mv "$file" "${file%.fsa_nt.4}.fa"
	done

done

# Now the blastoutput will be sorted from one strain with all the proteins in the file to one protein file with all
# the strains in it. It will be put in the folder ProteinFiles. The MergeLines folder is temporary.

    # Change the directory to the BlastOutput folder to retrieve the files of the strains containing
    # all of the proteins in them. things is the list in the directory containing all the strains with
    # a .fa extention. units is the variable for the individual strains in the list of things.

        #get the list of all strains(.fa) and set it as things. From the folder op protein/blastouput/
        things=($(ls | grep ".fa"))
        cd ../..

        #Set units as variable for all the strains in the things list.
        for units in ${things[*]}
        do

    #Read in the strainfile, called units, the first and third line and print them in a new file in
    # the directory MergeLines. The first line contains the protein name and the third line contains the
    # amino acid sequence.

            awk '{print $1, $13 }' Protein/BlastOutput/${units} > Protein/MergeLines/${units}

    #Now read the first and second column in the file. The first column is the protein name. This wil be
    # set a the name of the document in the folder ProteinFiles. This way, all proteins get their own document.
    # units, which is the strain name, will be printed in the first line of the document to create a fasta
    # header. second will be printed on the line beneath units, to paste in the amino acid sequence.
        done
        cd Protein/MergeLines

        objects=($(ls | grep ".fa"))
        cd ../..

        #Set units as variable for all the strains in the things list.
        for strains in ${objects[*]}
        do


	        while read -r first second
	            do
		            printf "\n>${strains}\n" >> Protein/ProteinFiles/${first}.fa
		            printf "${second}" >> Protein/ProteinFiles/${first}.fa

	            done < Protein/MergeLines/${strains}

        done

cd Protein/ProteinFiles/
echo "$PWD"

output=($(ls | grep ".fa"))

cd ..

for fastaSeq in ${output[*]}
do
clustalo -i ProteinFiles/${fastaSeq} -o Clustal/${fastaSeq} --outfmt=clustal -v --dealign --force
#for clustalw use, insert following command: $clustalw -INFILE=ProteinFiles/${fastaSeq} -OUTFILE=Clustal/${fastaSeq}
#seaview -plotonly Clustal/${fastaSeq}

done

# Removing the .fa extension of the protein comparison files in the Clustal folder
cd Clustal/
find . -name '*.fa' -type f | while read NAME ; do mv "${NAME}" "${NAME%.fa}" ; done

printf "\nAll tasks completed \n"