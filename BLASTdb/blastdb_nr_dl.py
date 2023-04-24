#! python3

import os
import urllib.request

'''
Downloads nr and nt blast databases to current working directory.
Will automatically retry download if it fails.

##Instructions for use
Before executing, go to url to check latest number of files.
Run "python3 ../path/to/blastdb_nr_dl.py" in ../blastdb/ directory.

https://ftp.ncbi.nlm.nih.gov/blast/db/
*.tar.gz
*tar.gz.md5
'''
parent_dir=os.getcwd() #../blastdb/
if not os.path.isdir('nr'):
    os.mkdir('nr')
nr_dir=parent_dir+'/nr/' #../blastdb/nr/

urllib.request.urlretrieve('https://ftp.ncbi.nlm.nih.gov/blast/db/nr-prot-metadata.json',nr_dir+'nr-prot-metadata.json')

nr=0
nr_max=67

while nr <= nr_max:
    nr_str = str(nr).zfill(2) #string with leading 0
    gz_file = 'nr.'+nr_str+'.tar.gz' #'nr.00.tar.gz'
    md5_file = gz_file+'.md5' #'nt.00.tar.gz.md5'

    gz_path = nr_dir+gz_file
    md5_path = gz_path+'.md5'

    try:
        if os.path.exists(gz_path):
            print('Removing existing '+gz_file)
            os.remove(gz_path)
            print('Removed '+gz_file+' file')
        if os.path.exists(md5_path):
            print('Removing existing '+md5_file)
            os.remove(md5_path)
            print('Removed '+md5_file+' file')
        print('Downloading '+gz_file)
        urllib.request.urlretrieve('https://ftp.ncbi.nlm.nih.gov/blast/db/'+gz_file,gz_path)
        print('Downloaded '+gz_file)
        print('Downloading '+md5_file)
        urllib.request.urlretrieve('https://ftp.ncbi.nlm.nih.gov/blast/db/'+md5_file,md5_path)
        print('Downloaded '+md5_file)
        nr = nr+1
    except:
        print('Download of '+gz_file+' interrupted.')
        if os.path.exists(gz_path):
            os.remove(gz_path)
            print('Incomplete '+gz_file+' file deleted. Trying again.')
        if os.path.exists(md5_path):
            os.remove(md5_path)
            print('Incomplete '+md5_file+' file deleted. Trying again.')