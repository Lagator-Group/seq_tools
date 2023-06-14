#! python3

import subprocess

threads=8

def main():
    featurecounts='featureCounts -a genomic.gtf -p -T '+str(threads)+' -t CDS -g gene_id -o featureCounts_table.txt *bam'
    print(featurecounts)
    subprocess.call(featurecounts,shell=True)

if __name__ == "__main__":
    main()