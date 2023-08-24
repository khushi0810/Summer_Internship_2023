import os
import shutil
import subprocess

env_dir = "../environment"

# Prompt the user to submit a text file
file_path = input("Please enter the path to the text file: ")

# Read the contents of the text file
with open(file_path, "r") as file:
    lines = file.readlines()

# Check if all required fields are provided
required_fields = ["project_name", "hic_data", "cutrun_data", "mouse_genome", "enhancer_filename", "peak_filenames"]
if len(lines) < len(required_fields):
    print("Error: Some required fields are missing in the text file.")
    exit(1)

# Extract the information from the text file
project_name, hic_data, cutrun_data, mouse_genome, enhancer_filename, peak_filenames = [line.strip() for line in lines]

# Check if hic_data, cutrun_data and mouse_genome values are valid
human_genomes = ["hg19", "hg38"]
mouse_genomes = ["mm10", "mm39"]
if hic_data.lower() not in human_genomes or cutrun_data.lower() not in human_genomes or mouse_genome.lower() not in mouse_genomes:
    print("Error: Invalid data provided for hic_data, cutrun_data or mouse_genome.")
    print("For hic_data and cutrun_data, only 'hg19' or 'hg38' are allowed.")
    print("For mouse_genome, only 'mm10' or 'mm39' are allowed.")
    exit(1)

# Check if project directory already exists
if os.path.exists(project_name):
    user_input = input(f"Project '{project_name}' already exists. Do you want to use this project (Y/N)? ")
    if user_input.lower() != "y":
        project_name = input("Enter a new project name: ")

# Create project directory if it doesn't exist
os.makedirs(project_name, exist_ok=True)

# Copy required files to project directory
snake_file = f"{hic_data}{cutrun_data}{mouse_genome}.snake"
for file in [snake_file, "khushi.py", "qwe.py", "rty.py", enhancer_filename,"references.txt"]:
    shutil.copy(file, project_name)

# Convert peak filenames string to a list
peak_list = [filename.strip() for filename in peak_filenames.split(",")]

# Copy peak files to project directory
for peak_file in peak_list:
    shutil.copy(peak_file, project_name)

# Read the reference files
with open("references.txt", "r") as file:
    references = file.readlines()

# Copy reference files to the project directory
for reference in references:
    reference = reference.strip()
    reference_file = f"{reference}.bw"
    shutil.copy(reference_file, project_name)
# Set the working directory to the project directory
os.chdir(project_name)

snakemake_command = [
    "snakemake",
    "-s", snake_file,
    "--cores", "16",
    "--jobs", "16",
    "--config", f"peaks={peak_list}", f"enhancer_file={enhancer_filename}", f"env_dir={env_dir}",
    "--cluster", "qsub -cwd -P langchip",
    "--latency-wait", "60"
]


# If the cutrun_data or hic_data is "hg38", download liftOver and set executable permissions
if "hg38" in {hic_data.lower(), cutrun_data.lower()}:
    subprocess.run(["wget", "http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/liftOver"])
    subprocess.run(["chmod", "+x", "liftOver"])

# Execute the Snakemake command
subprocess.run(snakemake_command)
