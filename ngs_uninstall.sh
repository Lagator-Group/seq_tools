#!/bin/bash

#run by executing "bash -i ngs_uninstall.sh"

#sra
conda remove -n sra --all

#filtlong
conda remove -n filtlong --all

#unicycler
conda remove -n unicycler --all

#abricate
conda remove -n abricate --all

#prokka
conda remove -n prokka --all
