# Summer_Internship_2023

Title : Building a pipeline for discovering transcription factor specific distal enhancer elements regulating gene expression in melanoma Cells

Mentors : Dr.Deborah Lang , Dr.Stephen Moore , Dr. Chao Zhang 

*  Manual: Contains the steps for using the pipeline 

*  Code : Contains the scripts for the pipeline
    - hic.py - Generates a csv file for enhncaers from 3DIV 
    - environment.py - For setting up the environment. which downloads the files that are needed for snakemake to run
    - selector.py - Takes input a text file from the user with different parameters
    - Snakamake files - Conatins bash commands for the pipeline depending upon users input
    - khushi.py - for letting know the snakemkae files if there are multiple inputs for peaks or just a single input
    - qwe.py - Generating combined csv file when there is one input for peaks
    - rty.py - Generating combined csv file when there are multiple inputs for peaks
    - references.txt - For histone enhancer markers

*  Sample_Files : Contains the required files for our first trial ( gene = ARPC5, cell line = SK-MEL5 cell line, Transcription factor = YAP,TAZ, Histone markers = H3K27me3,H3K4me3 ,H3K27Ac )
