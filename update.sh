#!/bin/bash

#run by executing "bash -i update.sh"

#filtlong
conda activate filtlong
conda update -c bioconda filtlong

#unicycler
conda activate unicycler
conda update -c bioconda unicycler

#abricate
conda activate abricate
conda update -c bioconda abricate

#pandas
conda activate pandas
conda update -c conda-forge pandas

#trim-galore
conda activate trim-galore
conda update -c bioconda trim-galore