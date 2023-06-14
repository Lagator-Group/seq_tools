#! python3

import os
import subprocess
from configparser import ConfigParser

config=ConfigParser()
config.read('seq_tools/config.ini')

sys_specs=config['sys_specs']
threads=sys_specs['threads']

def bam():
    try:
        os.mkdir('BAM')
    except:
        pass

    for sam in os.listdir('Bowtie2_SAM'):
        bam=sam.replace('.sam','')
        samtools='samtools view -bS Bowtie2_SAM/'+sam+' -@ '+str(threads)+' > BAM/'+bam+'.bam'
        print(samtools)
        subprocess.call(samtools,shell=True)

def sort():
    try:
        os.mkdir('BAM_sorted')
    except:
        pass
    for bam in os.listdir('BAM'):
        _sorted=bam.replace('.bam','_sorted.bam')
        sort='samtools sort BAM/'+bam+' -@ '+str(threads)+' -o BAM_sorted/'+_sorted
        print(sort)
        subprocess.call(sort,shell=True)

def index():
    sorted_list=[]
    for file in os.listdir():
        if file.endswith('_sorted.bam'):
            sorted_list.append(file)
    for _sorted in sorted_list:
        _index='samtools index BAM_sorted/'+_sorted+' -@ '+str(threads)
        print(_index)
        subprocess.call(_index,shell=True)

if __name__ == "__main__":
    bam()
    sort()
    index()