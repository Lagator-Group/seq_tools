# Sequence Alignment and Annotation
## Environment Preparation
All scripts can only be run within Linux. All scripts were developed in WSL.
Instructions on how to install WSL can be found [here](https://learn.microsoft.com/en-us/windows/wsl/install).

It is strongly recommended to use conda for each package. Several bash scripts in this repo assume you have conda installed. A setup.sh script is included to create all the necessary environments and install the appropriate packages.
Instructions to install Anaconda can be found [here](https://gist.github.com/kauffmanes/5e74916617f9993bc3479f401dfec7da).

To create all the conda envs and install all the relevant packages run ```bash -i setup.sh``` and press "y" when prompted.

## Sequenc Assembly Tools
Each module will be explained individually how they are currently being used. The combined instructions will be detailed at the later.
The settings detailed below are the default settings and are not optimised for specific assembly formats (i.e. plasmids). Please consult relevant GitHub pages for more info on the various packages.

### [Filtlong.](<https://github.com/rrwick/Filtlong>)
To install filtlong, run ``` conda install -c bioconda filtlong```

Used to removed low quality reads from long reads only.
Run ```python3 ../path/to/filtlong.py``` in the directory containing ```.fastq``` files.
Runs the following line of code for all .fastq files in directory:
```
filtlong --min_length 1000 --keep_percent 95 --target_bases 500000000 SEQ.fastq | gzip > filtlong/SEQ.fastq.gz'
```

Input: All ```long-read.fastq``` files in current directory. Output: ```fastq.gz``` in current directory

### [Unicycler](https://github.com/rrwick/Unicycler)
To install, run ```conda install -c bioconda unicycler```.

To use if you have multiple raw reads (both long and short).
Will identify long reads and short read pairs and run the appropriate command.
Run ```python3 ../path/to/unicycler.py``` in directory containing ```.fastq```, ```.fastq.gz```.

Long reads cannot have '_' in their name as that is how the script determines what is a long or short read.

Short reads will execute the following command:
```
unicycler -1 shortread_1.fastq -2 shortread_2.fastq -o uni_short/
```
Long reads will execute the following command:
```
unicycler -l longread.fastq -o uni_long/
```

If there are twice as many short reads than long reads, will perform hybrid assembly as well:
```
unicycler -1 short_1.fastq -2 short_2.fastq -l long.fastq -o uni_hybrid/
```
Input: All ```.fastq``` and ```fastq.gz``` in current directory.
Output: ```assembly.fasta``` in ```uni_long/short/hybrid/``` in current directory.


### [Flye](https://github.com/fenderglass/Flye/)
To install, run ```conda install -c bioconda flye```.

Use ```python3 ../path/to/flye.py``` to assemble each individual ```longname.fastq``` with following command:
```
flye -o flye --threads 8 --nano-raw longread.fastq

```
Input: All ```.fastq``` and ```.fastq.gz``` long reads in current directory.
Output: ```assembly.fasta``` in ```flye/``` in current directory.

### [Raven](https://github.com/lbcb-sci/raven)
To install, run ```conda install -c bioconda raven-assembler ```.

Use ```python3 ../path/to/raven.py``` to assemble each individual ```longname.fastq``` with following command:
```
raven --threads 8 longread.fastq > raven/assembly.fasta

```
Input: All ```.fastq``` and ```.fastq.gz``` long reads in current directory.
Output: ```assembly.fasta``` in ```raven/``` in current directory.
