import os
from os import *

while True:
    arg = input("Please type your input: \n help - List help commands")
    if arg == "help":
        print("inst:<package> - Installs a package")
        print("list:pkgs - List packages")
    if arg == "list:pkgs":
        print("wsl-get Packages:")
        print("gh - GitHub CLI")
    if arg == "inst:gh":
        os.system('wget https://github.com/cli/cli/releases/download/v2.14.1/gh_2.14.1_linux_amd64.deb')
        os.system('sudo apt install gh_2.14.1_linux_amd64.deb')
