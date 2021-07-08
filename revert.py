#!/bin/python3
from os import system
import modules.check_root as isRoot


def revert():
    Should_I_revert = input("Do you want me to revert all the changes?[y/N]: ")
    if(Should_I_revert == "y" or Should_I_revert == "Y"):
        print("Use timeshft gui for this....")
        # For fixing the relabling issue
        system("touch /root/.autorelabel")
        print("If you face any problem like login loop,\nuse your bootable disk and run this command as super user.\n\n")
        print("touch /root/.autorelabel")
        print("\n\nThis will tell your os to relabel every partition. And Fix the login loop issue caused due to timeshift")


revert()
