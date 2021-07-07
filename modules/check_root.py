import os


def check_Root():
    if os.getuid() != 0:
        print("I need Root Permissions!")
        return 0
    return 1
