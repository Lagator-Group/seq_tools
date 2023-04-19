#! python3

import subprocess
import os

'''
Require filtlong to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
<https://anaconda.org/bioconda/filtlong>
<https://github.com/rrwick/Filtlong>

##Instructions for use
Run 'python3 ../path/to/filtlong_all.py' in directory cotanining .fastq files.

Input: All .fastq files in current directory
Output: fastq.gz in filtlong/ directory
'''

def main():
    long_list=[]
    for seq in os.listdir(): 
        if seq.endswith('.fastq') or seq.endswith('fastq.gz'):
            if seq.endswith('_1.fastq') or seq.endswith('_1.fastq.gz') or seq.endswith('_2.fastq') or seq.endswith('_2.fastq.gz'): #ensure no short reads are added to list
                continue 
            else:
                long_list.append(seq)  #adds long-reads to list
    n=0
    _n=len(long_list)
    mkdir='mkdir pre_filtlong'
    subprocess.call(mkdir,shell=True)
    
    for seq in long_list:
        mv='mv '+seq+' pre_filtlong'
        subprocess.call(mv,shell=True)
        filtlong='filtlong --min_length 1000 --keep_percent 95 --target_bases 500000000 pre_filtlong/'+seq+' | gzip > '+seq+'.gz'
        subprocess.call(filtlong,shell=True)
    
if __name__ == "__main__":
    if os.path.isdir('pre_filtlong'):
        quit()
    else:
        main()