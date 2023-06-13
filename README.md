# Auto Push

Auto Push is a Python script that automates the process of committing and pushing changes to a Git repository. It prompts you to select a file, enter a commit message, and then automatically performs the commit and push operations.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
2. Navigate to the directory

    ```bash
    cd Auto_Push

3. Move the push file to the executable directory

    ```bash
    sudo mv push /usr/local/bin/

4. Make it Executable

    ```bash
    chmod +x /usr/local/bin/push

5. Done

## 🚀 Usage

1. type push on the terminal

    ```bash
    push

2. Select The file you wanna add and type the commit message
    
    ```bash
    ____________________________________
    / ____| |   |  __ \| |   | |__   __|
    | |  __| |   | |__) | |   | |  | |   
    | | |_ | |   |  _  /| |   | |  | |   
    | |__| | |___| | \ \| |___| |  | |   
    \_____|_____|_|  \_\______|  |_|   

    Enter the name of the file to commit:
    1) README.md
    2) test.py
    Select the file number: 1
    Enter Commit Message: Update Readme

    //Pushing.......
    [main d9725c8] 
    file changed, 4 insertions(+), 3 deletions(-)
    Enumerating objects: 5, done.
    Counting objects: 100% (5/5), done.
    Delta compression using up to 2 threads
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (3/3), 297 bytes | 148.00 KiB/s, done.
    Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
    remote: Resolving deltas: 100% (1/1), completed with 1 local object.
    To https://github.com/fletcher429/Auto_Push.git
   5b7723a..d9725c8  HEAD -> main
   Commit pushed successfully to GitHub.


3. NOTES

    ### READ
    1. ⚠️ Make sure you have Git installed on your system before using Auto Push.
    2. 📁 The push file has been moved to a directory in your system's PATH, enabling you to use the push command from any directory in the terminal.
    3. 🧩 Feel free to customize the push script or integrate it into your workflow as needed                                    