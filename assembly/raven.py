#! python3

import subprocess
import os
from configparser import ConfigParser
import shutil

'''
Requires raven to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
Will ONLY work on long reads. Will automatically ignore short reads.
Assumes you are running on raw nanopore reads
<https://anaconda.org/bioconda/raven-assembler>
<https://github.com/lbcb-sci/raven>

##Instructions for use
Run 'python3 ../path/to/raven.py' in directory containing .fastq or filtlong/
For long read, '_' cannot be in file name

Input: All .fastq or fastq.gz in current directory. If filtlong/ in directory, will search sequences inside
Output: Folder(s) in current directory. If there is a filtlong/ directory, results will be in that directory
'''
config=ConfigParser()
config.read('seq_tools/config.ini')

sys_specs=config['sys_specs']
threads=sys_specs['threads']

def main():
    long_list=[]
    for seq in os.listdir(): #groups sequences into short and long reads
        if seq.endswith('.fastq') or seq.endswith('fastq.gz'):
            if '_' not in seq:
                long_list.append(seq)

    n=0
    for seq in long_list:
        folder=str(n)+'raven'
        try:
            try:
                shutil.rmtree(folder)
            except:
                os.mkdir(folder)
            raven='raven --threads '+str(threads)+' +seq+ > '+str(n)+'raven/assembly.fasta'
            print(raven)
            subprocess.call(raven,shell=True)
        except:
            print('Something went wrong running raven on'+seq)
            continue
        finally:
            n=n+1             

if __name__ == "__main__":
    main()