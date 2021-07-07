from os import system

# Basic softwares installation
system("dnf install code git zsh gcc curl wget vim neovim")

# ZSH Syntax highlighting.
system("dnf install zsh-syntax-highlighting")

# Gnome specific programs
gnome_setup = input("Do you want me to install gnome tools")
if(gnome_setup == "Y" or gnome_setup == "y"):
    system("dnf install gnome-tweak-tool")
    system("dnf install gnome-extensions-app")

# Appending zsh in bashrc file
system("echo zsh >> ~/.bashrc")

# Installing OH-MY-ZSH
system("""sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" """)

# Flutter Installation
if(input("Do you want to install Flutter?[y/N]") != "N"):
    print("Cloning Flutter")
    system("git clone https://github.com/flutter/flutter.git")
    system("""export PATH="$PATH:`pwd`/flutter/bin" """)
    system("dnf install clang cmake ninja-build pkg-config libgtk-3-dev")
    system("""echo export PATH="$PATH:`pwd`/flutter/bin" >> ~/.bashrc """)
    system("flutter precache")

    # Installing Android studio.

    # Installing requests library to make a network call to get ip addr
    system("pip3 install requests")
    import requests
    try:
        r = requests.get("http://ipconfig.me")
        ipaddr = r.text

    except:
        print("something gone wrong!")
    system(
        f"wget https://r2---sn-hpjgvnj5o-cvhe.gvt1.com/edgedl/android/studio/ide-zips/4.2.2.0/android-studio-ide-202.7486908-linux.tar.gz?cms_redirect=yes&mh=Ug&mip={ipaddr}&mm=28&mn=sn-hpjgvnj5o-cvhe&ms=nvh&mt=1625660895&mv=m&mvi=2&pcm2cms=yes&pl=24&rmhost=r3---sn-hpjgvnj5o-cvhe.gvt1.com&shardbypass=yes&smhost=r1---sn-hpjgvnj5o-cvhs.gvt1.com")
# system("")
# system("")
