#! python3

import subprocess

def main():
    try:
        seqkit1='seqkit stats fastQ_trimmed_norRNA/*.fastq.gz > fastQ_trimmed_norRNA/seqkit_norRNA.txt' 
        seqkit2='seqkit stats fastQ_trimmed_rRNA/*.fastq.gz > fastQ_trimmed_rRNA/seqkit_rRNA.txt'

        subprocess.call(seqkit1,shell=True)
        subprocess.call(seqkit2,shell=True)
    except:
        print('Something went wrong running seqkit')
        pass

if __name__ == "__main__":
    main()