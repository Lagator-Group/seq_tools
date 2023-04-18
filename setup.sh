#!/bin/bash

#run by executing "bash -i setup.sh"

#filtlong
conda create -n filtlong
conda activate filtlong
conda install -c bioconda filtlong

#unicycler
conda create -n unicycler
conda activate unicycler
conda install -c bioconda unicycler

#flye
conda create -n flye
conda activate flye
conda install -c bioconda flye

#raven
conda create -n raven
conda activate raven
conda install -c bioconda raven-assembler

#abricate
