#!/bin/bash

assembly="/mnt/c/Users/jtdej/Desktop/GitHub/seq_tools/assembly

conda activate filtlong
python3 "${assembly}/filtlong.py"
conda activate unicycler
python3 "${assembly}/unicycler.py"
conda activate raven
python3 "${assembly}/raven.py"
conda activate flye
python3 "${assembly}/flye_ont.py"