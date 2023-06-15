#! python3

import os
import subprocess

'''
Requires bbmap to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
<https://anaconda.org/bioconda/bbmap>
<https://sourceforge.net/projects/bbmap>

##Instructions for use
Run 'python3 ../path/to/bbmap.py' in directory containing 'fastq_trimmed' directory, containing paired _1 and _2.fastq files.
Download ribokmers from <https://drive.google.com/file/d/0B3llHR93L14wS2NqRXpXakhFaEk/view?resourcekey=0-2fgNHw3hAtPFCSjJSVV-UQ>
and extract to seq_tools/ribokmers/ribokmers.fa

Input: All paired .fastq files. File names must be marked with _1 and _2 for forward and reverse reads, respectively.
Output: Trimmed sequences in 'fastq_trimmed_norRNA' directory.
'''

def main():
    n=0

    ref='seq_tools/ribokmers/ribokmers.fa' #path to ribokmers.

    #creates necessary directories if not already present
    try: #removes directory if it exists already to prevent errors
        os.rmdir('fastQ_trimmed_norRNA')
        os.rmdir('fastQ_trimmed_rRNA')
    except:    
        if not os.path.isdir('fastQ_trimmed_norRNA'):
            mkdir='mkdir fastQ_trimmed_norRNA'
        if not os.path.isdir('fastQ_trimmed_rRNA'):
            mkdir=mkdir+' fastQ_trimmed_rRNA'
        if len(mkdir)>0:
            subprocess.call(mkdir,shell=True)
    
    seq_list=[]
    for seq in os.listdir(): 
        if seq.endswith('_1.fastq') or seq.endswith('_1.fastq.gz'): #assumes _1 and _2 share same name and are both present
            seq_list.append(seq)

    for seq in seq_list:
        if seq.endswith('_1.fastq'): 
            _seq=seq.replace('_1.fastq','') #removes suffix from sequence file
        elif seq.endswith('_1.fastq.gz'):
            _seq=seq.replace('_1.fastq.gz','')

        val1=_seq+'_1_val_1.fq'
        val2=_seq+'_2_val_2.fq'

        bbduk='bbduk.sh in=fastq_trimmed/'+val1+' in2=fastq_trimmed/'+val2+\
            ' out=fastQ_trimmed_norRNA/'+_seq+'_1.fastq.gz out2=fastQ_trimmed_norRNA/'+_seq+'_2.fastq.gz '\
            'outm=fastQ_trimmed_rRNA/'+_seq+'_1.fastq.gz outm2=fastQ_trimmed_rRNA/'+_seq+'_2.fastq.gz '\
            'k=31 ref='+ref
        print(bbduk)
        subprocess.call(bbduk,shell=True)

        n=n+1
        
if __name__ == "__main__":
    main()