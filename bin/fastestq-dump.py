#! python3

import subprocess
import os
from configparser import ConfigParser
import shutil
'''
##Instructions for use
SRR_Acc_List.txt must 1 contain SRR code per line.
Run 'python3 ../path/to/fastestq-dump.py' in directory containing SRR_Acc_List.txt
'''
config=ConfigParser()
config.read('seq_tools/config.ini')

sys_specs=config['sys_specs']
threads=sys_specs['threads']
memory=sys_specs['memory']

def main():
    sra_list=[]
    parent_dir = os.getcwd()
    file_path = os.path.join(parent_dir, 'SRR_Acc_List.txt')
        
    with open(file_path, 'r') as f:
        for line in f:
            line=line.replace('\n','') #Removes unseen \n from MS .txt file. Should still work with UNIX .txt files
            sra_list.append(line)
    
    for sra in sra_list:
        try:
            print('Prefetching .sra for '+sra) #Prefetching first before running fasterq-dump is faster than fasterq-dump alone.
            prefetch='prefetch '+sra
            print(prefetch)
            subprocess.call(prefetch,shell=True)
        except:
            print('There was an error prefetching '+sra)
            continue
        try:
            print('Generating fastq for '+sra)
            fasterq_dump='fasterq-dump --threads '+str(threads)+' --mem '+str(memory)+'GB '+sra 
            print(fasterq_dump)
            subprocess.call(fasterq_dump,shell=True)
        except:
            print('There was error generating .fastq file for'+sra)
            continue
            
    for sra in sra_list:
        shutil.rmtree(sra)

if __name__ == "__main__":
    main()