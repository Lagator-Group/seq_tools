#!/bin/bash

# run with "bash -i seq_tools/assembly_plasmid.sh" from directory containing sequence files
# assembles and annotates plasmid usig prokka

conda activate filtlong
python3 "seq_tools/bin/filtlong.py"

conda activate unicycler
python3 "seq_tools/bin/unicycler.py"

conda activate abricate
python3 "seq_tools/bin/abricate_plasmid.py"

conda activate base
python3 "seq_tools/bin/contig_selector.py"

conda activate prokka
python3 "seq_tools/bin/prokka.py"