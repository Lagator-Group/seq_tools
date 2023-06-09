#! python3

import subprocess

'''
Requires seqkit to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
<https://anaconda.org/>
<https://github.com/>

##Instructions for use
Run 'python3 ../path/to/seqkit.py' in directory containing 'fastq_trimmed_norRNA' and 'fastq_trimmed_rNA' directories, containing paired _1 and _2.fastq files.

Input: All paired .fastq files. File names must be marked with _1 and _2 for forward and reverse reads, respectively.
Output: Stats on the trimmed sequences in the 'norRNA' and 'rRNA' directories.
'''

def main():
    seqkit1='seqkit stats fastQ_trimmed_norRNA/*.fastq.gz > fastQ_trimmed_norRNA/seqkit_norRNA.txt' 
    seqkit2='seqkit stats fastQ_trimmed_rRNA/*.fastq.gz > fastQ_trimmed_rRNA/seqkit_rRNA.txt'

    subprocess.call(seqkit1,shell=True)
    subprocess.call(seqkit2,shell=True)

if __name__ == "__main__":
    main()