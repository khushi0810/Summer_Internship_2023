import subprocess
import sys

# Get input files from command line arguments
input_files = sys.argv[1:]

# Based on the number of input files, choose which script to execute
if len(input_files) == 1:
    script_to_execute = 'rty.py'
else:
    script_to_execute = 'qwe.py'

# Create the command to execute
# The command is the name of the script followed by the list of input files
command = ['python', script_to_execute] + input_files

# Execute the command
subprocess.run(command)

