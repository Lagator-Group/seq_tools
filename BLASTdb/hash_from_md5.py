#! python3

def read_md5(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        lines = str(lines)
        #lines = lines[2:-18]
        lines = str(lines)
        lines = lines[2:-17]
        print(lines)

md5_dir = 'M:\\BLASTdb\\nt\\'
md5_ext = '.tar.gz.md5'

n=0
n_max=75

while n <= n_max:
    n_str = str(n).zfill(2) #string with leading 0
    md5 = md5_dir+'nt.'+n_str+md5_ext
    read_md5(md5)
    n=n+1