#!/bin/bash

# run with "bash -i seq_tools/contig_plasmid.sh" from directory containing sequence files

conda activate abricate
python3 "seq_tools/annotation/abricate_plasmid.py"
conda activate pandas
python3 "seq_tools/contig_selection/contig_selector.py"