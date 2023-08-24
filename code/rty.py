import pandas as pd
import sys
import os

# Get input files from command line arguments
input_files = sys.argv[1:]

# Combine the data from all input files
combined_df = pd.DataFrame()
for file in input_files:
    df = pd.read_csv(file)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# Group by enhancer coordinates and aggregate peaks
combined_df['peak'] = combined_df['peak_name'] + '(' + combined_df['peak_start'].astype(str) + '-' + combined_df['peak_end'].astype(str) + ')'
grouped_df = combined_df.groupby(['enhancer_chromosome', 'enhancer_start', 'enhancer_end'])['peak'].apply(', '.join).reset_index()

# Save the grouped data to a new CSV file
grouped_df.to_csv("combined_enhancers.csv", index=False)
