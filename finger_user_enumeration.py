#!/usr/bin/env python3

# Author: dev-angelist (https://github.com/dev-angelist)
# Version: 1.0

import subprocess
import sys
import os
import pyfiglet
from datetime import datetime

# Constants
default_finger_port = 79  # Default Finger port
query_timeout = 5  # Timeout for query (in seconds)

# Generate ASCII art banner for "Finger User Enumeration"
ascii_banner = pyfiglet.figlet_format("Finger User Enumeration", font="slant")
print(ascii_banner)

def print_section_header(text, char="="):
    """Function to print section headers with a separator."""
    separator = char * (len(text) + 4)
    print(separator)
    print(f"|  {text}  |")
    print(separator)

def print_help():
    """Function to print the help message."""
    print(f"==================================================================================\n")
    print("""Usage: python3 finger_user_enumeration.py -t <target> -w <wordlist> [-p <port>]

Options:
    -t <target>    : Target hostname or IP address (e.g., sunday.htb)
    -w <wordlist>  : Path to a wordlist of usernames (e.g., users.txt)
    -p <port>      : Custom port for the finger service (default: 79)
    -h, --help     : Show this help message and exit
    
Example of usage:
    python3 finger_user_enumeration.py -t sunday.htb -w users.txt -p 79
    """)
    print(f"==================================================================================\n")
def print_scan_info(target, wordlist, port):
    """Function to print scan information."""
    # Get current time, removing milliseconds
    scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Count the number of usernames in the wordlist
    num_usernames = sum(1 for _ in open(wordlist))

    # Unified print format
    print(f"===========================================================")
    print(f"|  Scanning target: {target} on port {port} for {num_usernames} usernames")
    print(f"|  Scanning started at: {scan_time}")    
    print(f"===========================================================\n")
    
def print_results(valid_users):
    """Function to print the final results."""
    if valid_users:
        for user in valid_users:
            print(f"[+] User found: {user}")
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
    port = default_finger_port

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
    print_results(valid_users)  # Print valid users only once

if __name__ == "__main__":
    main()
