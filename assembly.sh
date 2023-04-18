#$ -cwd

conda activate filtlong
python3 pwd/seq_tools/filtlong/filtlong.py

conda activate unicycler
python3 pwd/seq_tools/unicycler/unicycler.py

conda activate flye
python3 pwd/seq_tools/flye/flye.py

conda activate raven
python3 pwd/seq_tools/raven/raven.py