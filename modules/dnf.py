
def Check_If_Fedora():
    Distribution = 'Fedora'

    # opening a text file
    file = open("/etc/os-release", "r")

    # read file content
    readfile = file.read()

    # checking condition for string found or not
    if Distribution in readfile:
        print("Ohh yeah, It's Fedora")
        file.close
        return 1
    else:
        print("This script is currently limited to fedora only")
        file.close
        return 0
