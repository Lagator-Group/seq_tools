#! python3

import subprocess
import os

'''
Require flye to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
Will ONLY work on long reads. Will automatically ignore short reads.
Assumes you are running on raw nanopore reads
<https://anaconda.org/bioconda/flye>
<https://github.com/fenderglass/Flye/>

##Instructions for use
Run 'python3 ../path/to/flye.py' in directory containing .fastq or filtlong/
For long read, '_' cannot be in file name

Input: All .fastq or fastq.gz in current directory. If filtlong/ in directory, will search sequences inside
Output: Folder(s) in current directory. If there is a filtlong/ directory, results will be in that directory
'''
def main():
    filtlong=False
    long_list=[]
    if os.path.isdir('filtlong'):
        filtlong=True
        os.chdir('filtlong') #makes filtlong/ current working directory
    for seq in os.listdir(): 
        if seq.endswith('.fastq') or seq.endswith('fastq.gz') and '_2' not in seq and '_1' not in seq: #ensure no short reads are added to list
            long_list.append(seq) #adds long-reads to list

    if len(long_list)>0:
        for seq in long_list:
            if filtlong==True:
                flye='flye -o ../flye --nano-raw -t 8'+seq
            else:
                flye='flye -o flye --nano-raw -t 8'+seq
            subprocess.call(flye,shell=True)                

if __name__ == "__main__":
    main()