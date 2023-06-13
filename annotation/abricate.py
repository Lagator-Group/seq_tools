#! python3

import glob
import os
import subprocess

'''
Requires assembly to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
<https://anaconda.org/bioconda/abricate>
<https://github.com/tseemann/abricate/>

##Instructions for use
Run 'python3 ../path/to/abricate.py' in directory containing directories, each containing ../assembly.fasta

Input: All assembly.fasta in subdirectories.
Output: Summaries in abricate/ directory.
'''

def main():
    assembly=glob.glob('**/assembly.fasta', recursive=True) #generates list of all "assembly.fasta" in subdirectories
    print(assembly)
    tab_list=[]

    for fasta in assembly:
        name=fasta[:-15]+'.tab'
        tab_path='abricate/'+name
        tab_list.append(tab_path)
        print(name)

        try: #removes existing directory to prevent errors
            os.rmdir('abricate')
        finally:
            os.mkdir('abricate')

    tab_string=" ".join(tab_list)
    summary='abricate --summary '+tab_string+'> abricate/summary.tab'
    print(summary)
    subprocess.call(summary,shell=True)

if __name__=="__main__":
    main()