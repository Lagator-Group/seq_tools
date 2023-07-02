#! python3

import os
import subprocess
import shutil

'''
currently doesnt work on UoM CSF. issue with prokka and blastp
'''

def main():
    if os.path.isdir('contigs_plasmid'):
        for file in os.listdir('contigs_plasmid'):
            name=file.replace('.fasta','')
            folder='prokka_plasmid_'+name

            prokka='prokka --outdir '+folder+' --prefix '+name+' '+file
            subprocess.call(prokka,shell=True)

if __name__=="__main__":
    main()