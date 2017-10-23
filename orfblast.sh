#!/bin/bash

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/orf"

makeblastdb -in CLFA.fa -dbtype prot -out DB.fa

cp DB.fa.psq DB.fa

blastp -query QueryClfA.fa -db DB.fa -outfmt 6 -out blast.out
