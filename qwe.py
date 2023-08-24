import csv
import os
import sys

# Get input files from command line arguments
input_files = sys.argv[1:]

# Define the output file path
output_file = "combined_enhancers.csv"

# Initialize a dictionary to store enhancer information
enhancers = {}

# Process input files
for input_file in input_files:
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            chrom = row['enhancer_chromosome']
            start = row['enhancer_start']
            end = row['enhancer_end']
            peak = row['peak_name']
            peak_start = row['peak_start']
            peak_end = row['peak_end']

            # Extract the unique peak name based on the alphabets before the first underscore
            unique_peak_name = peak.split('_')[0]

            # Check if the enhancer already exists in the dictionary
            if (chrom, start, end) in enhancers:
                # Append peak information to existing enhancer
                enhancers[(chrom, start, end)][3] += f", {unique_peak_name} ({peak_start}-{peak_end})"
            else:
                # Create a new enhancer entry
                enhancers[(chrom, start, end)] = ['', '', '', f"{unique_peak_name} ({peak_start}-{peak_end})"]

# Write combined enhancers to output file
with open(output_file, 'w', newline='') as output:
    writer = csv.writer(output)
    writer.writerow(['enhancer_chromosome', 'enhancer_start', 'enhancer_end', 'peaks'])
    for (chrom, start, end), values in enhancers.items():
        writer.writerow([chrom, start, end, values[3]])