#!/bin/python3
from os import system
from time import sleep
import modules.check_root as isRoot
import modules.fastest_Mirror as FM
from modules.dnf import pacMan
system("echo Script Starting..")
# os.system("NAME=Fedora")

if isRoot.check_Root() == 0:
    exit()


FM.Check_FastestMirror()
print("Enabling RPM Fusion repo")
system("dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm")
system("dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm")
system(pacMan() + " update")


# END of program part
print("Groups you can try out")
sleep(3)
system("dnf grouplist -v")
print("To install any environment do\nsudo dnf install [environment name]")
print("For example: sudo dnf install @cinnamon-desktop-environment")
