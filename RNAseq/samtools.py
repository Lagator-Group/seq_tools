#! python3

import os
import subprocess

threads=8

def main():
    try:
        os.mkdir('BAM')
    except:
        pass

    for sam in os.listdir('Bowtie2_SAM'):
        bam=sam.replace('.sam','')
        samtools='samtools view -bS Bowtie2_SAM/'+sam+' -@ '+str(threads)+' > BAM/'+bam+'.bam'
        print(samtools)
        subprocess.call(samtools,shell=True)

if __name__ == "__main__":
    main()