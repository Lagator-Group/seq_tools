#! python3

import os
import urllib.request

'''
Downloads nt blastdb to current working directory.
Will automatically retry download if it fails.

##Instructions for use
Before executing, go to url to check latest number of files.
Run "python3 ../path/to/blastdb_nt_dl.py" in ../blastdb/ directory.

https://ftp.ncbi.nlm.nih.gov/blast/db/
*.tar.gz
*tar.gz.md5
'''
parent_dir=os.getcwd() #../blastdb/
if not os.path.isdir('nt'): 
    os.mkdir('nt')
nt_dir=parent_dir+'/nt/' #../blastdb/nt/

nt=0 #change this number if you've already partially downloaded the database (e.g to 15 if last download is 17 to make sure all incompletes are removed)
nt_max=91

urllib.request.urlretrieve('https://ftp.ncbi.nlm.nih.gov/blast/db/nt-nucl-metadata.json',nt_dir+'nt-nucl-metadata.json')

while nt <= nt_max:
    nt_str = str(nt).zfill(2) #string with leading 0
    gz_file = 'nt.'+nt_str+'.tar.gz' #'nt.00.tar.gz'
    md5_file = gz_file+'.md5' #'nt.00.tar.gz.md5'

    gz_path = nt_dir+gz_file
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
        nt = nt+1
    except:
        print('Download of '+gz_file+' interrupted')
        if os.path.exists(gz_path):
            os.remove(gz_path)
            print('Incomplete '+gz_file+' file deleted. Trying again')
        if os.path.exists(md5_path):
            os.remove(md5_path)
            print('Incomplete '+md5_file+' file deleted. Trying again')