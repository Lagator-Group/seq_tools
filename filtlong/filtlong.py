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
    align_list=[]
    for name in os.listdir():
        if name.endswith('.fastq'): 
            align_list.append(name)
    n=0
    _n=len(align_list)
    mkdir='mkdir filtlong'
    subprocess.call(mkdir,shell=True)
    for seq in align_list:
        print(seq)
        filtlong='filtlong --min_length 1000 --keep_percent 95 --target_bases 500000000 '+seq+' | gzip > filtlong/'+seq+'.gz'
        subprocess.call(filtlong,shell=True)

        n=n+1
        print(n,'/',_n,' done')
    
if __name__ == "__main__":
    main()