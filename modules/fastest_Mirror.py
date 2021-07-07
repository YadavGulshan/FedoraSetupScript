import os


def Check_FastestMirror():
    FastestMirror = 'fastestmirror=1'

    # opening a text file
    file = open("/etc/dnf/dnf.conf", "r")

    # read file content
    readfile = file.read()

    # checking condition for string found or not
    if FastestMirror in readfile:
        print("Fastest Mirrors are already set...")
        file.close
        return 1
    else:
        # Appending fastestmirror=1 in dnf conf file
        os.system("echo fastestmirror=1 >> /etc/dnf/dnf.conf")
        file.close
        return 0


def parallel_Download():
    # Configuring max parallel downloads to 10
    os.system("echo max_parallel_downloads=10 >> /etc/dnf/dnf.conf")
