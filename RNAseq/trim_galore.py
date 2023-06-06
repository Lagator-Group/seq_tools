#! python3

import os
import subprocess

threads=4

def main():
    n=0
    seq_list=[]
    for seq in os.listdir(): #groups sequences into short and long reads
        if seq.endswith('_1.fastq') or seq.endswith('_1fastq.gz'):
            seq_list.append(seq)

    for seq in seq_list:
        _1=str(seq)
        _2=str(_1.replace('_1.fastq','_2.fastq')) #assumes there is a corresponding _2 in folder

        trim_galore='trim_galore --paired '+_1+' '+_2+' -q 20 --phred33 --fastqc --length 50 fastq_trimmed/ '+str(threads)
        subprocess.call(trim_galore,shell=True)

        n=n+1
        
if __name__ == "__main__":
    main()