#! python3

import subprocess
from configparser import ConfigParser
'''
Requires subread to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
<https://anaconda.org/bioconda/subread>
<https://subread.sourceforge.net/>

##Instructions for use
Run 'python3 ../path/to/featurecount.py' in directory containing BAM_sorted directory, containing '.bai' and '.bam' files.

Input: .bam and .bai files
Output: featurecounts_table.txt
'''
config=ConfigParser()
config.read('seq_tools/config.ini')

sys_specs=config['sys_specs']
threads=sys_specs['threads']

def main():
    featurecounts='featureCounts -a genomic.gtf -p -T '+str(threads)+' -t CDS -g gene_id -o featureCounts_table.txt BAM_sorted/*.bam'
    print(featurecounts)
    subprocess.call(featurecounts,shell=True)

if __name__ == "__main__":
    main()