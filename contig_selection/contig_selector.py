#! python3

import os
import pandas as pd

def get_contig(tab):
    df=pd.read_csv(tab,sep='\t',usecols=['#FILE','SEQUENCE']) #opens tab file as pd.df
    _n=df.shape[0] #get number of rows in df
    n=0
    
    while n<_n: #will only run for number of rows in pd.df
        file=str(df['#FILE'][n]) #looks at reach row 'n' of pd.df
        contig='>'+str(df['SEQUENCE'][n]) #looks at corresponding contig code
        with open(file,'r') as f: #opens file identified in pd.df
            data=f.read()
            start=data.find(contig) #starts at contig identified in pd.df
            end=data.find('>', start+1) #determines end of contig with '>'
            result=data[start:end] #isolates contig from '>' from '>'

            if 'plasmid' in tab: #if 'plasmid' in filename, creates contig_plasmid folder
                contig_directory='contigs_plasmid'
            else:
                contig_directory='contigs' #else just creates contig folder
            if not os.path.isdir(contig_directory):
                os.mkdir(contig_directory)

            _fname=str(df['#FILE'][n])[:-15]
            fname=_fname+'_'+str(df['SEQUENCE'][n])+'.fasta' #final file name example = 0flye_contig_1.fasta
            path=contig_directory+'/'+fname #contigs/0flye_contig_1.fasta
            print(path)
            with open(path, 'w') as f:
                f.write(result) #outputs selected contigs to appropriate .fasta file
            f.close()

        n=n+1

def main():
    cwd=os.getcwd()
    abricate_folders=[f for f in os.listdir(cwd) if 'abricate' in f \
                      and os.path.isdir(os.path.join(cwd, f))] #selects all folders with the name 'abricate' in it
    
    tab_files=[]
    for root, dirs, files in os.walk(cwd): #gets all the .tab files in subdirectories
        for file in files:
            if file.endswith('.tab'):
                tab_files.append(file)
    tab_files.remove('summary.tab') #removes summary.tab from list
    
    tab_path=[]
    for folder in abricate_folders: #creates path for each .tab file
        for file in tab_files:
            path=folder+'/'+file
            tab_path.append(path)

    for tab in tab_path:
        get_contig(tab)

if __name__=="__main__":
    main()