from os import system


def initialize_print():
    print("Running your program so that it can be initialized.")


def flatpak_setup():
    flatpak = input("Do you want me to setup flatpak?[y/N]: ")
    if (flatpak == "Y" or flatpak == "y"):
        print("Installing flatpak")
        system("dnf install flatpak")
        system(
            "flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
        system("flatpak update")


def my_flatpak_apps():
    postman = input("Do you want to install Postman?[y/N]: ")

    if(postman == "y" or postman == "Y"):
        print("Installing Postman using flatpak")
        system("flatpak install flathub com.getpostman.Postman")
        initialize_print()
        system("flatpak run com.getpostman.Postman")

    freecad = input("Do you want to install Freecad?[Y/N]: ")

    if (freecad == "y" or freecad == "Y"):
        system("flatpak install flathub org.freecadweb.FreeCAD")
        initialize_print()
        system("flatpak run org.freecadweb.FreeCAD")
