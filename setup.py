#!/usr/bin/python3
import os
import subprocess
from main.tools import banner, colors
import cybertool


def exit_program():
    os.system("clear")
    banner.main()
    print("\033[38;5;105m", "[+] Thanks visit again".title())
    exit()


try:
    def main():
        os.system("clear")
        banner.main()
        banner.attack("Setup")
        os.system("pip install -r requirements.txt")
        os.system("sudo apt install golang -y")
        os.system("go env -w GO111MODULE=on")
        os.system("apt install php")
        create_symlink()


    def create_symlink():
        proc = subprocess.Popen([f"pwd"], stdout=subprocess.PIPE, shell=True)
        # there keyfor success output and noththere for error output
        (there, notthere) = proc.communicate()
        there = there.decode()
        there = there.split()
        f = open("run.sh", "w")
        f.write("#!/bin/bash")
        f.write("\n")
        f.write(f'cd {there[0]} && python3 cybertool.py "$@"')
        f.close()
        os.system("chmod +x *")
        os.system("sudo mv run.sh /usr/bin/cybertool")
        finish()


    def finish():
        os.system("clear")
        banner.main()
        banner.attack("Setup Completed")
        cybertool.main()


    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    exit_program()
except Exception as err:
    os.system("clear")
    banner.main()
    banner.attack(f"{colors.red}ERROR{colors.reset}")
    banner.description(f"{colors.red}{err}{colors.reset}")
