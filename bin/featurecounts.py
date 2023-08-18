#! python3

import subprocess
from configparser import ConfigParser
import os

config=ConfigParser()
config.read('seq_tools/config.ini')

sys_specs=config['sys_specs']
threads=sys_specs['threads']

def main():
    for file in os.listdir():
        if file.endswith('.gtf'):
            gtf=file
    try:
        featurecounts='featureCounts -a '+gtf+' -p -T '+str(threads)+' -t CDS -g gene_id -o featureCounts_table.txt BAM_sorted/*.bam'
        print(featurecounts)
        subprocess.call(featurecounts,shell=True)
    except:
        print('Something went wrong running featureCounts')
        pass

if __name__ == "__main__":
    main()