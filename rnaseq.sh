#!/bin/bash

conda activate trim-galore
python3 seq_tools/RNAseq/trim_galore.py

conda activate bbmap
python3 seq_tools/RNAseq/bbmap.py

conda activate seqkit
python3 seq_tools/seqkit.py