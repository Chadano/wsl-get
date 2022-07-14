import os
from os import *

while True:
    arg = input("Please type your input (type help to list commands):\n")
    if arg == "help":
        print("inst:<package> - Installs a package")
        print("list:pkgs - List packages")
        print("exit")
    if arg == "list:pkgs":
        print("wsl-get Packages:")
        print("gh - GitHub CLI")
    if arg == "inst:gh":
        os.system('wget https://github.com/cli/cli/releases/download/v2.14.1/gh_2.14.1_linux_amd64.deb')
        os.system('sudo apt install ./gh_2.14.1_linux_amd64.deb')
    if arg == "exit":
        quit()
