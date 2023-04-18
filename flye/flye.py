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
    n=0
    _n=len(long_list)
    while n<_n:
        seq=long_list[n]
        if filtlong==True:
            flye='flye -o ../'+n+'flye --nano-raw '+seq+' -t 8'
        else:
            flye='flye -o '+n+'flye --nano-raw '+seq+' -t 8'
        subprocess.call(flye,shell=True)                
        n=n+1

if __name__ == "__main__":
    main()