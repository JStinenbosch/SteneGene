#!/bin/bash

cd "$HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/retrieved/test/"

awk '/^>/{s=++d".fasta"} {print > s}' RF122.fa
