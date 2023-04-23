#!/bin/bash

contig_selection="/mnt/c/Users/jtdej/Desktop/GitHub/seq_tools/contig_selection"

conda activate abricate
python3 "${contig_selection}/abricate_plasmid.py"
conda activate pandas
python3 "${contig_selection}/contig_selector.py"