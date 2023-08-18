#! python3

import os
import subprocess
import shutil

'''
currently doesnt work on UoM CSF. issue with prokka and blastp
'''

def prokka(file):
    name=file.replace('.fasta','')
    folder='prokka_plasmid_'+name

    try:
        shutil.rmtree(folder)
    except:
        pass

    prokka='prokka --outdir '+folder+' --prefix '+name+' '+file
    subprocess.call(prokka,shell=True)

def main():
    if os.path.isdir('contigs_plasmid'):
        for file in os.listdir('contigs_plasmid'):
            if file.endswith('.fasta'):
                prokka(file)
    else:
        for file in os.listdir():
            if file.endswith('.fasta'):
                prokka(file)


if __name__=="__main__":
    main()