#!/bin/bash

conda activate trim-galore
python3 RNAseq/trim_galore.py

conda activate bbmap
python3 RNAseq/bbmap.py

conda activate seqkit
python3 seqkit.py