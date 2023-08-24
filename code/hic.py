import csv
import argparse

# Create the parser and add arguments
parser = argparse.ArgumentParser(description='Process enhancers.txt to CSV.')
parser.add_argument('--input', metavar='input', type=str, help='The path of input file.')
parser.add_argument('--output', metavar='output', type=str, help='The name of output file.')
args = parser.parse_args()

# Read the txt file and extract data
with open(args.input, 'r') as f:
    lines = f.readlines()

# Prepare data for the csv file
data = []
for line in lines:
    elements = line.split('\t')
    chr_start_end = elements[1].split(':')
    if len(chr_start_end) == 2:  # Add this check
        chromosome = chr_start_end[0]
        start, end = chr_start_end[1].split('-')
        data.append([chromosome, start, end])
    else:
        print(f"Skipped line: {line}")  # Or handle it differently

# Write data to the csv file
with open(args.output, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['chromosome', 'start', 'stop'])
    writer.writerows(data)
