#! python3

import os
import subprocess
from configparser import ConfigParser
import shutil
'''
Requires samtools to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
<https://anaconda.org/bioconda/samtools>
<https://github.com/samtools/samtools>

##Instructions for use
Run 'python3 ../path/to/samtools.py' in directory containing Bowtie2_SAM directory, containing '.sam' files.

Input: .sam files
Output: .bam files in BAM_sorted directory
'''
config=ConfigParser()
config.read('seq_tools/config.ini')

sys_specs=config['sys_specs']
threads=sys_specs['threads']

def bam():
    try:
        shutil.rmtree('BAM')
    except:
        pass
    os.mkdir('BAM')

    for sam in os.listdir('Bowtie2_SAM'):
        try:
            bam=sam.replace('.sam','')
            samtools='samtools view -bS Bowtie2_SAM/'+sam+' -@ '+str(threads)+' > BAM/'+bam+'.bam'
            print(samtools)
            subprocess.call(samtools,shell=True)
        except:
            print('Something went wrong running samtools view on '+sam)
            continue

def sort():
    try:
        shutil.rmtree('BAM_sorted')
    except:
        pass
    os.mkdir('BAM_sorted')

    for bam in os.listdir('BAM'):
        try:
            _sorted=bam.replace('.bam','_sorted.bam')
            sort='samtools sort BAM/'+bam+' -@ '+str(threads)+' -o BAM_sorted/'+_sorted
            print(sort)
            subprocess.call(sort,shell=True)
        except:
            print('Something went wrong running samtools sort on'+bam)
            continue

def index():
    sorted_list=[]
    for file in os.listdir():
        try:
            if file.endswith('_sorted.bam'):
                sorted_list.append(file)
        except:
            print('There are no _sorted.bam files to sort')
            continue
    for _sorted in sorted_list:
        try:
            _index='samtools index BAM_sorted/'+_sorted+' -@ '+str(threads)
            print(_index)
            subprocess.call(_index,shell=True)
        except:
            print('Something went wrong runnning samtools index on '+_sorted)
            continue

if __name__ == "__main__":
    bam()
    sort()
    index()