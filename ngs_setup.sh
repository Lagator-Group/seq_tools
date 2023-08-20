#!/bin/bash

#run by executing "bash -i ngs_setup.sh"

#pandas
conda install -c conda-forge pandas

#sra
conda env create -f env/sra.yml

#filtlong
conda env create -f env/filtlong.yml

#unicycler
conda env create -f env/unicycler.yml

#abricate
conda env create -f env/abricate.yml

#prokka
conda env create -f env/prokka.yml
