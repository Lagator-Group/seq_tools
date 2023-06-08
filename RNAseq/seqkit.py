#! python3

import subprocess

def main():
    seqkit1='seqkit stats fastQ_trimmed_norRNA/*.fastq.gz > fastQ_trimmed_norRNA/seqkit_norRNA.txt' 
    seqkit2='seqkit stats fastQ_trimmed_rRNA/*.fastq.gz > fastQ_trimmed_rRNA/seqkit_rRNA.txt'

    subprocess.call(seqkit1,shell=True)
    subprocess.call(seqkit2,shell=True)

if __name__ == "__main__":
    main()