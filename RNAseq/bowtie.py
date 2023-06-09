#! python3

import subprocess
import os

'''
Requires bowtie to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
<https://anaconda.org/>
<https://github.com/>

##Instructions for use
Run 'python3 ../path/to/bowtie.py' in directory containing 'fastq_trimmed_norRNA' directory, containing paired _1 and _2.fastq.gz files.
Adjust thread number according to PC specs.
Download reference genome from NCBI and paste 'GCF' and 'genomic.gtf' files in directory containing original .fastq files
Adjust strain name depending on reference genome.

Input: All paired .fastq.gz files. File names must be marked with _1 and _2 for forward and reverse reads, respectively.
Output: .sam file in 'Bowtie2_SAM' directory.
'''

threads=8
strain='MG1655'

def main():
    fna=[]
    for file in os.listdir():
        if file.endswith('.fna'):
            fna.append(file)
    
    if len(fna)>1:
        print('Too many reference genomes in directory')
    elif len(fna)<1:
        print('There are not enough reference genomes in directory')
    
    print(fna[0])

    build='bowtie2-build --threads '+str(threads)+' '+fna[0]+' '+strain
    print(build)
    subprocess.call(build,shell=True)

    if not os.path.isdir('Bowtie2_SAM'):
        mkdir='mkdir Bowtie2_SAM'
        print(mkdir)
        subprocess.call(mkdir,shell=True)
    
    fastq=[]
    for file in os.listdir('fastQ_trimmed_norRNA'):
        if file.endswith('_1.fastq.gz'):
            fastq.append(file)
    for seq in fastq:
        sam=seq.replace('_1.fastq.gz','')    
        _1=seq
        _2=seq.replace('_1.fastq.gz','_2.fastq.gz')
        bowtie='bowtie2 -x '+strain+' -1 fastQ_trimmed_norRNA/'+_1+' -2 fastQ_trimmed_norRNA/'+_2+\
            ' -S Bowtie2_SAM/'+sam+'.sam --no-mixed --threads '+str(threads)
        print(bowtie)
        subprocess.call(bowtie,shell=True)
    
    '''
    if not os.path.isdir('refseq'):
            mkdir='mkdir refseq'
            subprocess.call(mkdir,shell=True)

    for file in os.listdir():
        if file.endswith('.bt2') or file.endswith('.fna') or file.endswith('.gtf'):
            move='mv '+file+' refseq'
            subprocess.call(move,shell=True)
    '''
if __name__ == "__main__":
    main()