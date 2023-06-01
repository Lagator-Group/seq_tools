#!/bin/bash

conda activate abricate
python3 "annotation/abricate_plasmid.py"
conda activate pandas
python3 "contig_selection/contig_selector.py"