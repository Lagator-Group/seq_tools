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
        _n=len(short_list)
        while n<_n:
            _1=str(short_list[n])
            _2=str(_1.replace('_1.fastq','_2.fastq')) #assumes there is a corresponding _2 in folder
            try:
                _name=_1.replace('.fastq.gz','')
            except:
                _name=_1.replace('.fastq','')
            print(_name)
            if len(filtlong)>0:
                unicycler='unicycler -1 '+_1+' -2 '+_2+' -o ../'+n+'uni_short/'
            else:
                unicycler='unicycler -1 '+_1+' -2 '+_2+' -o '+n+'uni_short/'
            subprocess.call(unicycler,shell=True)
            n=n+1
            print(n,'/',_n,' done')

    def long(long_list):
        n=0
        _n=len(long_list)
        for seq in long_list:
            try:
                _name=str(seq.replace('.fastq.gz',''))
            except:
                _name=str(seq.replace('.fastq',''))
            print(_name)
            if len(filtlong)>0:
                unicycler='unicycler -l '+seq+' -o ../'+n+'uni_long/'
            else:
                unicycler='unicycler -l '+seq+' -o '+n+'uni_long/'
            subprocess.call(unicycler,shell=True)
            n=n+1
            print(n,'/',_n,' done')
        
    def hybrid(short_list,long_list):
        n=0
        _n=len(long_list)
        while n<_n:
            _1=str(short_list[n])
            _2=str(_1.replace('_1.fastq','_2.fastq')) #assumes there is a corresponding _2 in folder
            _long=long_list[n]

            if len(filtlong)>0:
                unicycler='unicycler -1 '+_1+' -2 '+_2+' -l '+_long+' -o ../'+n+'uni_hybrid/'
            else:
                unicycler='unicycler -1 '+_1+' -2 '+_2+' -l '+_long+' -o '+n+'uni_hybrid/'
            subprocess.call(unicycler,shell=True)
            n=n+1

def main():
    short_list=[]
    long_list=[]
    if os.path.isdir('filtlong'): 
        filtlong.append(1)
        os.chdir('filtlong') #makes filtlong_out/ current working directory
    for seq in os.listdir(): 
        if seq.endswith('_1.fastq') or seq.endswith('_1.fastq.gz'): #selects _1 short-read file
            short_list.append(seq) #adds _1 short-read to list
        elif (seq.endswith('.fastq') or seq.endswith('fastq.gz')) and '_2.fastq' not in str(seq): #assumes all remaining sequences without _2 are long-reads
            long_list.append(seq) #adds long-reads to list

    if len(short_list)==len(long_list): #will only run hybrid assembly if there are exactly 2x number of shorts than long reads
        unicycler.hybrid(short_list,long_list)
    else:
        if len(short_list)>0:
            unicycler.short(short_list)
        if len(long_list)>0:
            unicycler.long(long_list)

if __name__ == "__main__":
    main()