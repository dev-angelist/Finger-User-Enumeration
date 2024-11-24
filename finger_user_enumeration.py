#!/usr/bin/env python3
# Author: dev-angelist (https://github.com/dev-angelist)

import subprocess
import sys
import os
import pyfiglet
from datetime import datetime

# Constants
VERSION = 1.0
AUTHOR = "@dev-angelist"
DEFAULT_FINGER_PORT = 79  # Default Finger port

# Generate ASCII art banner"
ascii_banner = pyfiglet.figlet_format("    Finger   User      Enumeration", font="slant")
print(ascii_banner)

def print_help():
    """Function to print the help message."""
    print(f"==================================================================================\n")
    print("""Usage: python3 finger_user_enumeration.py -t <target> -w <wordlist> [-p <port>]

Options:
    -t <target>    : Target hostname or IP address (e.g., sunday.htb)
    -w <wordlist>  : Path to a wordlist of usernames (e.g., users.txt)
    -p <port>      : Custom port for the finger service (default: 79)
    -h, --help     : Show this help message and exit

Wordlist Info:
    - You can download a usernames wordlist from SecLists:
        wget -O names.txt https://raw.githubusercontent.com/danielmiessler/SecLists/master/Usernames/Names/names.txt

    - If you're using Kali Linux, the wordlist is already available at:
        /usr/share/wordlists/wfuzz/others/names.txt

Example of usage:
    python3 finger_user_enumeration.py -t sunday.htb -w users.txt -p 79
    """)
    print(f"==================================================================================\n")

def print_scan_info(target, wordlist, port):
    scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    num_usernames = sum(1 for _ in open(wordlist))

    print(f"   =================================================================================")
    print(f"  /  Starting finger-user-enum v{VERSION} by {AUTHOR}")
    print(f" /  https://github.com/dev-angelist/Finger-User-Enumeration")
    print(f"/  Scanning target: {target} on port {port} for {num_usernames} usernames at: {scan_time}")
    print(f"====================================================================================\n")

def print_results(valid_users):
    """Function to print the final results."""
    if valid_users:
        for user in valid_users:
            print(f"[+] User found: {user}")
        print(f"\n[!] {len(valid_users)} Users Found")
    else:
        print("[-] No valid users found.")

def get_finger_output(target, username, port):
    """Function to get the finger output for a given user."""
    try:
        result = subprocess.check_output(f"finger {username}@{target} {port}", shell=True, stderr=subprocess.PIPE)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

def check_valid_user(output):
    """Function to check if the user is valid by analyzing the output."""
    if "Login" in output and "Name" in output and "Super-User" in output:
        return True
    if "ssh" in output:
        return True
    return False

def main():
    # Default port is 79, can be changed by user input
    port = DEFAULT_FINGER_PORT

    # Check if the user requested help
    if "-h" in sys.argv or "--help" in sys.argv:
        print_help()
        sys.exit(0)

    # Parse arguments
    if len(sys.argv) < 5:
        print("[!] Error: Invalid arguments.")
        print_help()
        sys.exit(1)

    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "-t":
            target = sys.argv[i + 1]
        elif sys.argv[i] == "-w":
            wordlist = sys.argv[i + 1]
        elif sys.argv[i] == "-p":
            port = int(sys.argv[i + 1])

    # Start the scan
    valid_users = []

    # Print scan information
    print_scan_info(target, wordlist, port)

    with open(wordlist, 'r') as f:
        for line in f:
            username = line.strip()
            output = get_finger_output(target, username, port)
            clean_output = " ".join(output.split())

            if check_valid_user(clean_output):
                valid_users.append(f"{username}@{target}")

    # Print results
    print_results(valid_users)

if __name__ == "__main__":
    main()
