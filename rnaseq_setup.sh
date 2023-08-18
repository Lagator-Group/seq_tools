#!/bin/bash

#run by executing "bash -i rnaseq_setup.sh"

#trim-galore
conda env create -f env/trim-galore.yml

#bbmap
conda env create -f env/bbmap.yml

#seqkit
conda env create -f env/bbmap.yml

#bowtie
conda env create -f env/bowtie.yml

#samtools
conda env create -f env/samtools.yml

#subreads
conda env create -f env/subread.yml
