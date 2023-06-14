#!/bin/bash

#make sure the file is in LF not CRLF
#run with "bash -i seq_tools/rnaseq.sh" from directory containing sequences

conda activate trim-galore
python3 seq_tools/RNAseq/trim_galore.py

conda activate bbmap
python3 seq_tools/RNAseq/bbmap.py

conda activate seqkit
python3 seq_tools/RNAseq/seqkit.py

conda activate bowtie
python3 seq_tools/RNAseq/bowtie.py

conda activate samtools
python3 seq_tools/RNAseq/samtools.py

conda activate subread
python3 seq_tools/RNAseq/featurecounts.py