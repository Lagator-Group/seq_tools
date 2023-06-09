#! python3

import subprocess
import os
import shutil
'''
Require sra-tools to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
<https://anaconda.org/bioconda/sra-tools>
<https://github.com/ncbi/sra-tools/wiki>

##Instructions for use
SRR_Acc_List.txt must 1 contain SRR code per line.
Run 'python3 ../path/to/fastestq-dump.py' in directory containing SRR_Acc_List.txt

Input: SRR## in SRR_Acc_List.txt
Output: .fastq files in current directory
'''
threads=8

def main():
    sra_list=[]
    parent_dir = os.getcwd()
    file_path = os.path.join(parent_dir, 'SRR_Acc_List.txt')
        
    with open(file_path, 'r') as f:
        for line in f:
            line=line.replace('\n','') #Removes unseen \n from MS .txt file. Should still work with UNIX .txt files
            sra_list.append(line)
    
    for sra in sra_list:
        print('Prefetching .sra for '+sra) #Prefetching first before running fasterq-dump is faster than fasterq-dump alone.
        prefetch='prefetch '+sra
        print(prefetch)
        subprocess.call(prefetch,shell=True)

        print('Generating fastq for '+sra)
        fasterq_dump='fasterq-dump --threads '+str(threads)+' --mem 14GB '+sra 
        print(fasterq_dump)
        subprocess.call(fasterq_dump,shell=True)
            
    for sra in sra_list:
        shutil.rmtree(sra)

if __name__ == "__main__":
    main()