import os
import subprocess

# Create the directory named 'environment'
os.makedirs('environment', exist_ok=True)

# Change to the new directory
os.chdir('environment')

# List of commands to be executed
commands = [
    "wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.fa.gz && gunzip hg19.fa.gz",
    "module load samtools && samtools faidx hg19.fa",
    "wget http://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz && gunzip hg38.fa.gz",
    "module load samtools && samtools faidx hg38.fa",
    "wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.14.0+-x64-linux.tar.gz && tar -xzf ncbi-blast-2.14.0+-x64-linux.tar.gz",
    "wget https://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/genes/hg19.ncbiRefSeq.gtf.gz && gunzip hg19.ncbiRefSeq.gtf.gz",
    "wget https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/genes/hg38.ncbiRefSeq.gtf.gz && gunzip hg38.ncbiRefSeq.gtf.gz",
    "wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/liftOver/hg19ToHg38.over.chain.gz && gunzip hg19ToHg38.over.chain.gz",
    "wget http://hgdownload.soe.ucsc.edu/goldenPath/hg38/liftOver/hg38ToHg19.over.chain.gz && gunzip hg38ToHg19.over.chain.gz",
    "wget https://hgdownload.soe.ucsc.edu/goldenPath/mm39/bigZips/mm39.fa.gz && gunzip mm39.fa.gz",
    "makeblastdb -in mm39.fa -dbtype nucl -parse_seqids -out mm39_db",
    "wget https://hgdownload.soe.ucsc.edu/goldenPath/mm10/bigZips/mm10.fa.gz && gunzip mm10.fa.gz",
    "makeblastdb -in mm10.fa -dbtype nucl -parse_seqids -out mm10_db",
    "wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/hg19.chrom.sizes",
    "chmod 777 hg19.chrom.sizes",
    "wget http://hgdownload.cse.ucsc.edu/goldenPath/hg38/bigZips/hg38.chrom.sizes",
    "chmod 777 hg38.chrom.sizes",
    "wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bedGraphToBigWig",
    "chmod +x bedGraphToBigWig"
]

# Execute each command
for command in commands:
    subprocess.call(command, shell=True)