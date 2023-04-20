#! python3

import glob

assembly=glob.glob('**/assembly.fasta', recursive=True)
print(assembly)