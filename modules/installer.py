from os import system


def input_value(program_name):
    return input(f"Do you want me to install {program_name} [y/N]: ")


def basic_installation():
    # Basic softwares installation
    system("dnf install code git zsh gcc curl wget vim neovim")

    # ZSH Syntax highlighting.
    system("dnf install zsh-syntax-highlighting")

    # Gnome specific programs
    gnome_setup = input_value("Gnome tweeks")
    if(gnome_setup == "Y" or gnome_setup == "y"):
        system("dnf install gnome-tweak-tool")
        system("dnf install gnome-extensions-app")

    # Appending zsh in bashrc file
    system("echo zsh >> ~/.bashrc")

    # Installing OH-MY-ZSH
    system("""sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" """)


def flutter():
    # Flutter Installation
    flutter = "N"
    flutter = input_value("Flutter")
    if(flutter == "Y" or flutter == "y"):
        print("Cloning Flutter")
        system("git clone https://github.com/flutter/flutter.git")
        system("""export PATH="$PATH:`pwd`/flutter/bin" """)
        system("dnf install clang cmake ninja-build pkg-config libgtk-3-dev")
        system("""echo export PATH="$PATH:`pwd`/flutter/bin" >> ~/.bashrc """)
        system("flutter precache")

        # Installing Android studio.

        # Installing requests library to make a network call to get ip addr
        print("Installing Requests library!")
        system("pip3 install requests")
        import requests
        try:
            r = requests.get("http://ipconfig.me/ip")
            ipaddr = r.text
            system(
                f"wget https://r2---sn-hpjgvnj5o-cvhe.gvt1.com/edgedl/android/studio/ide-zips/4.2.2.0/android-studio-ide-202.7486908-linux.tar.gz?cms_redirect=yes&mh=Ug&mip={ipaddr}&mm=28&mn=sn-hpjgvnj5o-cvhe&ms=nvh&mt=1625660895&mv=m&mvi=2&pcm2cms=yes&pl=24&rmhost=r3---sn-hpjgvnj5o-cvhe.gvt1.com&shardbypass=yes&smhost=r1---sn-hpjgvnj5o-cvhs.gvt1.com")
        except:
            print("something gone wrong!")
            print("Please download the android studio from their official site")
        print("Task Completed, Now uninstalling Requests library")
        system("pip3 uninstall requests")


def social():

    # Telegram Installation
    telegram = input_value("Telegram")
    if(telegram == "y" or telegram == "Y"):
        system("dnf install telegram-desktop")

    # Zoom installation
    zoom = input_value("Zoom")
    if(zoom == "y" or zoom == "Y"):
        system("dnf install zoom")

    # Discord Installation
    discord = input_value("discord")
    if(discord == "y" or zoom == "Y"):
        system("dnf install zoom")
