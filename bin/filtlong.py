#! python3

import subprocess
import os
import shutil

def main():
    long_list=[]
    for seq in os.listdir(): 
        if seq.endswith('.fastq') or seq.endswith('fastq.gz'):
            if seq.endswith('_1.fastq') or seq.endswith('_1.fastq.gz') or seq.endswith('_2.fastq') or seq.endswith('_2.fastq.gz'): #ensure no short reads are added to list
                continue 
            else:
                long_list.append(seq)  #adds long-reads to list
    n=0
    _n=len(long_list)
    os.mkdir('pre_filtlong')
    
    for seq in long_list:
        try:
            shutil.move(seq,'pre_filtlong/')
            filtlong='filtlong --min_length 1000 --keep_percent 95 --target_bases 500000000 pre_filtlong/'+seq+' | gzip > '+seq+'.gz'
            print(filtlong)
            subprocess.call(filtlong,shell=True)
        except:
            print('Something went wrong running filtlong on '+seq)
            continue
    
if __name__ == "__main__":
    if os.path.isdir('pre_filtlong'):
        print('Filtlong already done. Skipping')
        quit()
    else:
        main()