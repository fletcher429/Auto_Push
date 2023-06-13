#!/usr/bin/python3
import os
import subprocess
from colorama import init, Fore

# Initialize colorama
init()

# Logo ASCII art
logo = f"""{Fore.YELLOW}
   _____ _     _____  _     _ _______ 
  / ____| |   |  __ \| |   | |__   __|
 | |  __| |   | |__) | |   | |  | |   
 | | |_ | |   |  _  /| |   | |  | |   
 | |__| | |___| | \ \| |___| |  | |   
  \_____|_____|_|  \_\______|  |_|   
  BY DAVID & YVONNE
                                             
{Fore.RESET}"""

# Print the logo
print(logo)

# Check if Git is installed
try:
    subprocess.check_output(['git', '--version'])
except OSError as e:
    print(f"{Fore.RED}Git is not installed. Please install Git and try again.{Fore.RESET}")
    exit(1)

# Check if the user is in a Git repository
try:
    subprocess.check_output(['git', 'rev-parse', '--is-inside-work-tree'])
except subprocess.CalledProcessError as e:
    print(f"{Fore.RED}Not in a Git repository. Please navigate to a Git repository and try again.{Fore.RESET}")
    exit(1)

# Check if there are any changes to commit
git_status_output = subprocess.check_output(['git', 'status', '--porcelain']).decode().strip()
if git_status_output:
    print(f"{Fore.YELLOW}There are uncommitted changes. Adding all files to commit.{Fore.RESET}")
    subprocess.call(['git', 'add', '.'])

# Generate a list of files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Prompt for file name
print(f"{Fore.YELLOW}Enter the name of the file to commit:")
for i, file_name in enumerate(files, start=1):
    print(f"{i}) {file_name}")
selected_index = int(input("Select the file number: ")) - 1
file_name = files[selected_index]

# Prompt for commit message
commit_message = input("Enter the commit message: ")

# Commit the changes
subprocess.call(['git', 'commit', '-m', commit_message, file_name])

# Push the commit to the remote repository
if subprocess.call(['git', 'push', 'origin', 'HEAD']) == 0:
    print(f"{Fore.GREEN}Commit pushed successfully to GitHub.{Fore.RESET}")
else:
    print(f"{Fore.RED}Failed to push the commit to GitHub.{Fore.RESET}")
    exit(1)