
def Check_If_Fedora():
    Distribution = 'Fedora'

    # opening a text file
    file = open("/etc/os-release", "r")

    # read file content
    readfile = file.read()

    # checking condition for string found or not
    if Distribution in readfile:
        # print('String', Distribution, 'Found')
        file.close
        return 1
    else:
        # print('String', Distribution, 'Not Found')
        file.close
        return 0


def pacMan():
    if Check_If_Fedora() == 1:
        print("Fuck yeah it's Fedora.")
        return "dnf"
