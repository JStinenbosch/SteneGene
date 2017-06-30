#!/bin/bash

cd $HOME/Documents/Bovine_S.aureus_sequences/Nucleotide_sequences/

awk '/^>/{print s? s"\n"$0:$0;s="";next}{s=s sprintf("%s",$0)}END{if(s)print s}' FixedFiles/ProteinTest.fa > FixedFiles/ProteinTest2.fa

awk 'NR%2{printf "%s ",$0;next;}1' FixedFiles/ProteinTest2.fa > FixedFiles/ProteinTest3.fa
