#!/bin/bash

conda activate abricate
python3 "seq_tools/annotation/abricate_plasmid.py"
conda activate pandas
python3 "seq_tools/contig_selection/contig_selector.py"