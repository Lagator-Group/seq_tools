#! python3

import subprocess
import os
import shutil

'''
Requires bowtie to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
<https://anaconda.org/>
<https://github.com/>

##Instructions for use
Run 'python3 ../path/to/bowtie.py' in directory containing 'fastq_trimmed_norRNA' directory, containing paired _1 and _2.fastq.gz files.
Adjust thread number according to PC specs.
Download reference genome from NCBI and paste 'GCF###.fna' and 'genomic.gtf' files in directory containing original .fastq files
Adjust strain name depending on reference genome.

Input: All paired .fastq.gz files. File names must be marked with _1 and _2 for forward and reverse reads, respectively.
Output: .sam file in 'Bowtie2_SAM' directory.
'''

threads=8
strain='MG1655'

def main():
    #gets name of reference sequence (.fna)
    fna=[]
    for file in os.listdir():
        if file.endswith('.fna'):
            fna.append(file) 
    
    #ensures only 1 reference genome is present in the directory
    if len(fna)>1:
        print('Too many reference genomes in directory')
        quit()
    elif len(fna)<1:
        print('There are not enough reference genomes in directory')
        quit()
    
    print(fna[0])

    build='bowtie2-build --threads '+str(threads)+' '+fna[0]+' '+strain
    print(build)
    subprocess.call(build,shell=True)

    #create necessary SAM directory for output
    try:
        os.rmdir('Bowtie2_SAM') #removes if it already exists to prevent errors
    finally:
        os.mkdir('Bowtie2_SAM')

    fastq=[]
    for file in os.listdir('fastQ_trimmed_norRNA'):
        if file.endswith('_1.fastq.gz'):
            fastq.append(file) #assumes that _1 and _2 have same beginning of name
    for seq in fastq:
        sam=seq.replace('_1.fastq.gz','')    
        _1=seq
        _2=seq.replace('_1.fastq.gz','_2.fastq.gz')
        bowtie='bowtie2 -x '+strain+' -1 fastQ_trimmed_norRNA/'+_1+' -2 fastQ_trimmed_norRNA/'+_2+\
            ' -S Bowtie2_SAM/'+sam+'.sam --no-mixed --threads '+str(threads)
        print('The following command may take some time to complete.')
        print(bowtie)
        subprocess.call(bowtie,shell=True)
    
    try:
        os.rmdir('refseq')
    finally:
        os.mkdir('refseq')
    
    for file in os.listdir():
        if file.endswith('.bt2') or file.endswith('.fna') or file.endswith('.gtf'):
            shutil.move(file,'refseq/')
    
if __name__ == "__main__":
    main()