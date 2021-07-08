#!/bin/python3
from modules.flatpak import flatpak_setup, my_flatpak_apps
from os import system
from time import sleep, time
import modules.check_root as isRoot
from modules.fastest_Mirror import Check_FastestMirror, parallel_Download
from modules.dnf import pacMan
from modules.timeshift import timeshift
from modules.installer import basic_installation, flutter, input_value, social

system("echo Script Starting..")
# os.system("NAME=Fedora")

if isRoot.check_Root() == 0:
    exit()

# Creating a timeshift snapshot
timeshift("Before Setup")

# Changing to fastest mirror
Check_FastestMirror()

# Setting max Parallel download to 10
parallel_Download()


# RPM fussion
print("Enabling RPM Fusion repo")
system("dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm")
system("dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm")


# Update
system(pacMan() + " update")

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

restart = input("Do you want me to restart your pc?[y/N]: ")
if(restart == "y" or restart == "Y"):
    system("reboot")
