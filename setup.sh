#!/bin/bash

#run by executing "bash -i setup.sh"

#filtlong
conda create -n filtlong -c bioconda filtlong

#unicycler
conda create -n unicycler -c bioconda unicycler

#flye
conda create -n flye -c bioconda flye

#raven
conda create -n raven -c bioconda raven-assembler

#abricate
conda create -n abricate -c bioconda abricate

#pandas
conda create -n pandas -c conda-forge pandas

#trim-galore
conda create -n trim-galore -c bioconda trim-galore

#bbmap
conda create -n bbmap
#seqkit
conda create -n seqkit
#bowtie
conda create -n bowtie