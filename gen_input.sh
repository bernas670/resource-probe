#!/bin/bash

echo "Generating input for k-nucleotide benchmark"
python3 Python/Fasta/fasta-5.py 10000 > knucleotide-input10000.txt

echo "Generating input for reverse-complement benchmark"
python3 Python/Fasta/fasta-5.py 10000 > revcomp-input10000.txt

echo "Generating input for regex-redux benchmark"
python3 Python/Fasta/fasta-5.py 10000 > regexredux-input10000.txt