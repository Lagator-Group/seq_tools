# Sequence Alignment and Annotation
## Environment Preparation
All scripts can only be run within Linux. All scripts were developed in WSL.
Instructions on how to install WSL can be found [here](https://learn.microsoft.com/en-us/windows/wsl/install).

It is strongly recommended to use conda for each package. Several bash scripts in this repo assume you have conda installed. A setup.sh script is included to create all the necessary environments and install the appropriate packages.
Instructions to install Anaconda can be found [here](https://gist.github.com/kauffmanes/5e74916617f9993bc3479f401dfec7da).

To create all the conda envs and install all the relevant packages run ```bash -i setup.sh``` and press "y" when prompted.

## [Filtlong](<https://github.com/rrwick/Filtlong>)
To install filtlong, run ``` conda install -c bioconda filtlong```
###Instructions for Use
To use if you have many sequences if in directory you wish to use filtlong on.
Run ```python3 ../path/to/filtlong_all.py``` in the directory containing .fastq files.

 Input: All .fastq files in current directory. Output: fastq.gz in filtlong/ directory
