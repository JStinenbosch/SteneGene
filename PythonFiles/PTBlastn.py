import csv
import os
import sys
from Utilities import *

acceptable_extensions = ['.fasta', '.fas', '.fa', '.fsa', '.fna', '.fsa_nt']
CURRENT_DIR = os.getcwd()


# THIS PART WILL BE REPLACED BY GUI
def readInput():
    if len(sys.argv) < 2:
        print("Please specify input file")
        exit(-1)

    return sys.argv[1:]


# THIS PART WILL BE REPLACED BY GUI

def make_blast_db(files):
    os.makedirs("BlastDB",exist_ok=True)
    for sequence in files:
        os.system("makeblastdb -in " + sequence + " -dbtype nucl -out BlastDB/" + sequence)

def blast_query(files):
    os.makedirs("BlastOutput",exist_ok=True)
    for f in files:
        print("Blasting for " + f)
        os.system(
            "blastn -query ProteinQuery.fa -db BlastDB/" + f + " -out BlastOutput/" + f + "_raw" +
            " -outfmt \"10 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore sseq\"")

def find_value_in_blast(reader, column):
    for i, row in enumerate(reader):
        if i == column:
            print("This is the line." )
            print(row)
            break

def select_files():
    os.chdir("BlastOutput/")
    for f in os.listdir():
        with open(f + '_processed.fa', 'w') as wfd:
            file_reader = csv.reader(open(f,"r"))
            for row in file_reader:
                print(row)
                if int(row[4]) > 50:
                    wfd.write(",".join(row))


########################################################################################################################
#                                           Start of script                                                            #
########################################################################################################################

print("\nThis script blasts proteins to nucleotides (tblastn)\n\n")
print('''Getting in folder 'nucleotide_sequences' all files with the following extensions:
    .fasta, .fas, .fa, .seq, .fsa: Generic FASTA
    .fna, .fna_nt, .fsa_nt: FASTA nucleic acids\n
    But not the following extentions:
    .ffn: FASTA nucleotide coding regions for a genome
    .faa FASTA amino acids
    .mpfa: FASTA amino acides in multiple proteins
    .frn: FASTA non-coding RNA
    .fastq: FASTQ\n\n''')

if not os.path.exists(CURRENT_DIR + "/Nucleotide_sequences/"):
    print("Creating local directory /Nucleotide_sequences/")
    os.makedirs(CURRENT_DIR + "/Nucleotide_sequences/", exist_ok=True)
    print("Please add your nucleotide sequences to this directory")
    exit(-1)

files = readInput()
for name in files:
    if not name.endswith(tuple(acceptable_extensions)):
        print("Incorrect extension, we only allow " + str(acceptable_extensions))
        exit(-1)

query = handle_input_files(files)
make_blast_db(files)
print(files)
os.system("cd BlastDB && echo $PWD && echo databases have been produced")
blast_query(files)

select_files()


########################################################################################################################
#                                           End of script                                                              #
########################################################################################################################

'''

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
'''
