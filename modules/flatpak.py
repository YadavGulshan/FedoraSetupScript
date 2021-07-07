from os import system


def initialize_print():
    print("Running your program so that it can be initialized.")


postman = input("Do you want to install Postman?[Y/N]: ")
if(postman == "y" or postman == "Y"):
    print("Installing Postman using flatpak")
    system("flatpak install flathub com.getpostman.Postman")
    initialize_print()
    system("flatpak run com.getpostman.Postman")


freecad = input("Do you want to install Freecad?[Y/N\: ")

if (freecad == "Y" or freecad == "y"):
    system("flatpak install flathub org.freecadweb.FreeCAD")
    initialize_print()
    system("flatpak run org.freecadweb.FreeCAD")
