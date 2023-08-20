#!/bin/bash

#run by executing "bash -i rnaseq_uninstall.sh"

#trim-galore
conda remove -n trim-galore --all

#bbmap
conda remove -n bbmap --all

#seqkit
conda remove -n seqkit --all

#bowtie
conda remove -n bowtie --all

#samtools
conda remove -n samtools --all

#subread
conda remove -n subread --all

echo "done"
