from os import system


def timeshift(comment):
    system("dnf install timeshift")
    print("Creating a snapshot.")
    print("Please wait it will take some time.")
    system(f"""timeshift --create --comments "{comment}" --tags D""")
    print("Snapshot created, now we can start our work..")
