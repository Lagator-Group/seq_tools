#! python3

import glob
import os
import subprocess

def main():
    assembly=glob.glob('**/assembly.fasta', recursive=True) #generates list of all "assembly.fasta" in subdirectories
    csv_list=[]

    for fasta in assembly:
        name=fasta[:-15]+'.csv'
        csv_path='abricate/'+name
        csv_list.append(csv_path)
        print(name)

        if not os.path.isdir('abricate'):
            mkdir='mkdir abricate'
            subprocess.call(mkdir,shell=True)
        abricate='abricate '+fasta+' > abricate/'+name
        subprocess.call(abricate,shell=True)

        summary= #converts list into string separated by space    

if __name__=="__main__":
    main()