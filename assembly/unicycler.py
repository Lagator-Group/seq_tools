#! python3

import subprocess
import os

'''
Require unicycler to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
Will work with either short or long reads
If there are 2 short reads and 1 long read, will assume they are matched and also perform hybrid assembly
<https://anaconda.org/bioconda/unicycler>
<https://github.com/rrwick/Unicycler>

##Instructions for use
Run 'python3 ../path/to/unicycler.py' in directory containing .fastq or filtlong/
For long read, '_' cannot be in file name

Input: All .fastq or fastq.gz in current directory. If filtlong/ in directory, will search sequences inside
Output: Folder(s) in current directory. If there is a filtlong/ directory, results will be in that directory
'''
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

    if len(short_list)>0:
        unicycler.short(short_list)  
    if len(long_list)>0:
        unicycler.long(long_list)
    if len(short_list)==len(long_list): #will only run hybrid assembly if there are exactly the number of short_1 and long reads
        unicycler.hybrid(short_list,long_list)


if __name__ == "__main__":
    main()