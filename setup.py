#!/bin/python3
from modules.fonts import fonts
from modules.flatpak import flatpak_setup, my_flatpak_apps
from os import getcwd, system
from time import sleep, time
import modules.check_root as isRoot
from modules.fastest_Mirror import Check_FastestMirror, parallel_Download
from modules.dnf import Check_If_Fedora
from modules.timeshift import timeshift
from modules.installer import basic_installation, flutter, input_value, social

def Brand():
    print("""
  ▄████  █    ██  ██▓      ██████  ██░ ██  ▄▄▄       ███▄    █ 
 ██▒ ▀█▒ ██  ▓██▒▓██▒    ▒██    ▒ ▓██░ ██▒▒████▄     ██ ▀█   █ 
▒██░▄▄▄░▓██  ▒██░▒██░    ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█  ██▓▓▓█  ░██░▒██░      ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▒▓███▀▒▒▒█████▓ ░██████▒▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░
 ░▒   ▒ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
  ░   ░ ░░▒░ ░ ░ ░ ░ ▒  ░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░
░ ░   ░  ░░░ ░ ░   ░ ░   ░  ░  ░   ░  ░░ ░  ░   ▒      ░   ░ ░ 
      ░    ░         ░  ░      ░   ░  ░  ░      ░  ░         ░ 
\n\n\n\n
""")
print('██████ Please star the repo, https://github.com/YadavGulshan/FedoraSetupScript')
print('██████ Do check my blogs too, https://blog.BufferOverflow.me')
print('██████ Do follow me on github if you liked this project, https://github.com/YadavGulshan')


Brand()

# os.system("NAME=Fedora")
print("Checking if it's fedora")
if Check_If_Fedora() != 1:
    exit()

print("Checking if I have a root prevelege or not")
if isRoot.check_Root() == 0:
    exit()


print("Setting up the device to connect fastest mirror")
# Changing to fastest mirror
Check_FastestMirror()


print("Setting max parallel download to 10")
# Setting max Parallel download to 10
parallel_Download()


# RPM fussion
print("Enabling RPM Fusion")
system("dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm")
system("dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm")


print("Setting up timeshift")
# Creating a timeshift snapshot
timeshift("Before Setup")



# Copy repo to /etc/yum.repos.d for installing some programs
print("Adding required repositories to repos.d")
print("Please remove the unused repos from /etc/yum.repos.d")
def repo_Setup():
    pwd = getcwd()
    repo = pwd+"/repo"
    # print(repo)
    system(f"cp {repo}/*.repo /etc/yum.repos.d/")


repo_Setup()

# Update
system("dnf update")


print("Font's part")
# Fonts installation
fonts()

# Basic Installation
basic_installation()

# Flutter Installation
flutter()

# Social Apps installation
social()

# Some important flatpak setup
flatpak_setup()

# My flatpak apps
my_flatpak_apps()


# End of Script Timeshift
timeshift("The End")

# END of program part
print("Groups you can try out")
sleep(3)
system("dnf grouplist -v")
print("To install any environment do\nsudo dnf install [environment name]")
print("For example: sudo dnf install @cinnamon-desktop-environment")


# restart
restart = input("Do you want me to restart your pc?[y/N]: ")
if(restart == "y" or restart == "Y"):
    system("reboot")
