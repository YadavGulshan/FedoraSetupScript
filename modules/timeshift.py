from os import system


def timeshift():
    system("dnf install timeshift")
    print("Creating a snapshot.")
    print("Please wait it will take some time.")
    system("""timeshift --create --comments "before setup" --tags D""")
    print("Snapshot created, now we can start our work..")
