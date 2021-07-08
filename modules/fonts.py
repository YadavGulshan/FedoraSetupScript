from os import system


def fonts():
    font = input("Do you want to install MS fonts?[y/N]: ")
    if(font == "y" or font == "Y"):
        print("Please be patient, it may take a while")
        system("dnf install curl cabextract xorg-x11-font-utils fontconfig")
        system("rpm -i https://downloads.sourceforge.net/project/mscorefonts2/rpms/msttcore-fonts-installer-2.6-1.noarch.rpm")
