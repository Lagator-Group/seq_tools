#! python3

import os
import subprocess

threads=8

def main():
    for bam in os.listdir('BAM_sorted'):
        featurecounts='featureCounts -a refseq/genomic.gtf -p -T '+str(threads)+' -t CDS -g gene_id -o featureCounts_table.txt BAM_sorted/'+bam
        subprocess.call(featurecounts,shell=True)

if __name__ == "__main__":
    main()