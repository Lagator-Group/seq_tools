#!/bin/bash

#run by executing "bash -i setup.sh"

#filtlong
conda create -n filtlong -c bioconda filtlong

#unicycler
conda create -n unicycler -c bioconda unicycler

#flye
conda create -n flye -c bioconda flye

#raven
conda create -n raven
conda activate raven
conda install -c bioconda raven-assembler

#abricate
conda create -n abricate
conda activate abricate
conda install -c bioconda abricate