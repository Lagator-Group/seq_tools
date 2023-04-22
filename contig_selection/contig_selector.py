#! python3

import os
import glob

tab_files=[]

def main():
    cwd=os.getcwd()
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith(".tab"):
                tab_files.append(file)

    tab_files.remove('summary.tab')
    print(tab_files)

if __name__=="__main__":
    main()