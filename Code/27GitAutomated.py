#STIAGO
#!/usr/bin/env python27

import subprocess
import os

def update_file():
    filepath =  "/Python/Code/numbers.txt"
    command = "/usr/bin/git pull /Python/Code"
    process = subprocess.Popen(command, stdout = subprocess.PIPE ,stderr = subprocess.PIPE, shell=True)
    print process

def main():
    update_file()

if __name__ == "__main__":
    main()
