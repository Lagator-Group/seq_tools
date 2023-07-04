#!/bin/bash

# run with "bash -i seq_tools/assembly_plasmid.sh" from directory containing sequence files
# assembles and annotates plasmid usig prokka

conda activate filtlong
python3 "seq_tools/assembly/filtlong.py"
conda activate unicycler
python3 "seq_tools/assembly/unicycler.py"
conda activate flye
python3 "seq_tools/assembly/flye_ont_plasmid.py"
conda activate abricate
python3 "seq_tools/annotation/abricate_plasmid.py"
conda activate base
python3 "seq_tools/contig_selection/contig_selector.py"
conda activate prokka
python3 "seq_tools/annotation/prokka.py"