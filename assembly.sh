#!/bin/bash

conda activate filtlong
python3 "seq_tools/assembly/filtlong.py"
conda activate unicycler
python3 "seq_tools/assembly/unicycler.py"
conda activate raven
python3 "seq_tools/assembly/raven.py"
conda activate flye
python3 "seq_tools/assembly/flye_ont.py"