#!/bin/bash

conda activate filtlong
python3 Seq_Tools/filtlong/filtlong.py

conda activate unicycler
python3 Seq_Tools/unicycler/unicycler.py

conda activate flye
python3 Seq_Tools/flye/flye.py

conda activate raven
python3 Seq_Tools/raven/raven.py