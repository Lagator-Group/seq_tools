#!/bin/bash

conda activate filtlong
python3 seq_tools/filtlong/filtlong.py
conda activate unicycler
python3 seq_tools/unicycler/unicycler.py
conda activate raven
python3 seq_tools/raven/raven.py
conda activate flye
python3 seq_tools/flye/flye.py