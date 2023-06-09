#!/bin/bash

# run with "bash -i seq_tools/contig.sh" from directory containing sequence files

conda activate abricate
python3 "seq_tools/annotation/abricate.py"