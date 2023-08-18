#! python3

import subprocess
import os

filtlong=[]

class unicycler:
    def short(short_list):
        n=0
        for seq in short_list:
            try:
                _1=seq
                _2=str(_1.replace('_1.fastq','_2.fastq')) #assumes there is a corresponding _2 in folder
                unicycler='unicycler -1 '+_1+' -2 '+_2+' -o '+str(n)+'uni_short/'
                print(unicycler)
                subprocess.call(unicycler,shell=True)
            except:
                print('Something went wrong running unicycler_short on'+seq)
                continue
            finally:
                n=n+1

    def long(long_list):
        n=0
        for seq in long_list:
            try:
                unicycler='unicycler -l '+seq+' -o '+str(n)+'uni_long/'
                print(unicycler)
                subprocess.call(unicycler,shell=True)
            except:
                print('Something went wrong running unicycler_long on'+seq)
                continue
            finally:
                n=n+1
        
    def hybrid(short_list,long_list):
        n=0
        for seq in short_list:
            try:
                _1=seq
                _2=str(_1.replace('_1.fastq','_2.fastq')) #assumes there is a corresponding _2 in folder
                _long=long_list[n]
                unicycler='unicycler -1 '+_1+' -2 '+_2+' -l '+_long+' -o '+str(n)+'uni_hybrid/'
                print(unicycler)
                subprocess.call(unicycler,shell=True)
            except:
                print('Something went wrong running unicycler_hybrid on'+seq)
                continue
            finally:
                n=n+1

def main():
    short_list=[]
    long_list=[]
    for seq in os.listdir(): #groups sequences into short and long reads
        if seq.endswith('.fastq') or seq.endswith('fastq.gz'):
            if '_' not in seq: #'_' cannot be in file name
                long_list.append(seq)
            elif '_2' not in seq:
                short_list.append(seq)


    if len(short_list)==len(long_list): #will only run hybrid assembly if there are exactly the number of short_1 and long reads
        unicycler.hybrid(short_list,long_list)
    else:
        if len(short_list)>0:
            unicycler.short(short_list)  
        if len(long_list)>0:
            unicycler.long(long_list)

if __name__ == "__main__":
    main()