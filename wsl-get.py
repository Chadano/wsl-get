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
        print("lkc - Linux Kernel Compilation Devtools")
        print("omz - Oh-My-ZSH")
        print("qkvm - QEMU-KVM")
        print("nala - Nala")
    if arg == "inst:gh":
        os.system('wget https://github.com/cli/cli/releases/download/v2.14.1/gh_2.14.1_linux_amd64.deb')
        os.system('sudo apt install ./gh_2.14.1_linux_amd64.deb')
    if arg == "inst:lkc":
        os.system('sudo apt install build-essential libncurses-dev bison flex libssl-dev libelf-dev')
    if arg == "inst:omz":
        print("Make sure that you have a font with glyphs installed in case you want to install a theme that uses icons! You can download them at https://www.nerdfonts.com/")
        input("Press Enter to continue.")
        os.system('sudo apt install zsh')
        os.system('sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"')
    if arg == "inst:qkvm":
        os.system('sudo apt install qemu-kvm')
    if arg == "inst:nala":
        os.system('wget https://deb.volian.org/volian/pool/main/n/nala/nala_0.8.2_all.deb')
        os.system('sudo apt install ./nala_0.8.2_all.deb')
    if arg == "exit":
        quit()
