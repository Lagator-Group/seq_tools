#! python3

import os
import subprocess
from configparser import ConfigParser

'''
Requires trim-galore to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
<https://anaconda.org/bioconda/trim-galore>
<https://github.com/FelixKrueger/TrimGalore>

##Instructions for use
Run 'python3 ../path/to/trim_galore.py' in directory containing .fastq files
Adjust core number based on machine running the code.

Input: All paired .fastq files. File names must be marked with _1 and _2 for forward and reverse reads.
Output: Trimmed sequences in fastq_trimmed directory.
'''

config=ConfigParser()
config.read('seq_tools/config.ini')

sys_specs=config['sys_specs']
cores=sys_specs['cores']

def main():
    n=0
    seq_list=[]
    for seq in os.listdir(): #gets .fastq files in current directory
        try:
            if seq.endswith('_1.fastq') or seq.endswith('_1.fastq.gz'): #only gets _1 as it assumes _2 has identtical first section
                seq_list.append(seq)
        except:
            continue

    for seq in seq_list:
        try:
            _seq=seq.replace('_1.fastq','')
            _1=str(seq) 
            _2=str(_1.replace('_1.fastq','_2.fastq')) #assumes there is a corresponding _2 in folder

            trim_galore='trim_galore --paired '+_1+' '+_2+' -q 20 --phred33 --fastqc --length 50 -o fastq_trimmed/ -j '+str(cores)
            print(trim_galore)
            subprocess.call(trim_galore,shell=True)
        except:
            print('Something went wrong running trim-galore on '+_seq)
            continue
        n=n+1
        
if __name__ == "__main__":
    main()