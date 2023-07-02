#! python3

import glob
import os
import subprocess
import shutil

'''
Requires abricate to be installed and mapped to PATH to function
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

    try: #removes existing directory to prevent errors
        shutil.rmtree('abricate_plasmid')
    except:
        pass
    os.mkdir('abricate_plasmid')

    for fasta in assembly:
        try:
            name=fasta[:-15]+'.tab'
            tab_path='abricate_plasmid/'+name
            tab_list.append(tab_path)
            print(name)

            abricate='abricate -db plasmidfinder '+fasta+' > abricate_plasmid/'+name
            print(abricate)
            subprocess.call(abricate,shell=True)
        except:
            print('Something went wrong running abricate on'+fasta)
            continue
    
    try:
        tab_string=" ".join(tab_list)
        summary='abricate --summary '+tab_string+'> abricate_plasmid/summary.tab'
        print(summary)
        subprocess.call(summary,shell=True)
    except:
        print('Something went wrong running abricate --summary')

if __name__=="__main__":
    main()