#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date: 2023/04/21
import argparse
import os
import subprocess
import requests
import hashlib
from colors import *
from sys import argv

def main():
    banner = f"""{RED}
        ################################################      
        ##██████##██▓#███▄#▄███▓#██▓███###██▓####▓█████#
        ▒██####▒#▓██▒▓██▒▀█▀#██▒▓██░##██▒▓██▒####▓█###▀#
        ░#▓██▄###▒██▒▓██####▓██░▓██░#██▓▒▒██░####▒███###
        ##▒###██▒░██░▒██####▒██#▒██▄█▓▒#▒▒██░####▒▓█##▄#
        ▒██████▒▒░██░▒██▒###░██▒▒██▒#░##░░██████▒░▒████▒
        ▒#▒▓▒#▒#░░▓##░#▒░###░##░▒▓▒░#░##░░#▒░▓##░░░#▒░#░
        ░#░▒##░#░#▒#░░##░######░░▒#░#####░#░#▒##░#░#░##░
        ░##░##░###▒#░░######░###░░#########░#░######░###
        ######░###░#########░################░##░###░##░{WHITE}
        \t{GREEN}let go {WHITE}
    """
    os.system("clear")
    print(banner)
    parser = argparse.ArgumentParser(description="args")
    parser.add_argument("-t", "--tools", help="Install tools", nargs=1, type=str)
    parser.add_argument("-c", "--config", help="Configurate tools", nargs=1, type=str)
    args = parser.parse_args()
    distrib_id = os.popen("cat /etc/*-release | grep -w ID").read().replace("ID=","").strip()

    programs_file = open("progs_ubuntu.txt", "r")
    programs = [line.strip() for line in programs_file.readlines()]

    if args.config is not None:
        config = args.config[0].lower()
        if config == "ubuntu":
            if distrib_id == "ubuntu":
                subprocess.run("cd && mkdir tools && cd tools", shell=True)
                print(f"{GREEN}[+] {RESET} Installing golang {GREEN}[+]{RESET}")
                url = 
                for program in programs:
                    #subprocess.run(["echo", program])
                    print(f"Installing: {program}")
                print(f"{RED}done{RESET}")
                for program in programs:
                    #subprocess.run(["echo", program])
                    print(f"Installing: {program}")
                print(f"{RED}done{RESET}")
            else:
                print("[-] Not Ubuntu [-]")
    elif args.tools is not None:
        tool = args.tools[0].lower()
        if tool == "arch":
            # TODO
        else:
            print("Not working!!")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
