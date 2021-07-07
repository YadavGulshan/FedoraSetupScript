#!/bin/python3
import os
import modules.check_root as isRoot
import modules.fastest_Mirror as FM
from modules.dnf import pacMan
os.system("echo Script Starting..")
# os.system("NAME=Fedora")

if isRoot.check_Root() == 0:
    exit()


FM.Check_FastestMirror()
os.system(pacMan() + " update")
