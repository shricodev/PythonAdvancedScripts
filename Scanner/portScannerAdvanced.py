# AUTHOR: Shrijal Acharya(~YuShx01)

import re
import sys
import socket
import pyfiglet
import argparse
import threading
from termcolor import colored


def Scanner(tHost, tPort):
    '''This is the function that does every scans recursively with multiple threads'''
    try:
        # AF_INET FOR IPV4 AND SOCK_STREAM FOR TCP
        socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socks.connect((tHost, tPort))
        print(colored(f"[+] Port: {tPort}/tcp is Open", 'green'))
    except:
        print(colored(f"[-] Port: {tPort}/tcp is Closed", 'red'))
    finally:
        # Close the connection
        socks.close()


def portscanner(targetHost, targetPort):
    '''Does all the resolving works and uses threads to scan the target by calling a new function'''
    try:
        targetIP = socket.gethostbyname(targetHost)
    except:
        print(f"Could not Resolve the HOSTNAME: {targetHost}")
        sys.exit(1)

    try:
        # This try block is only executed if the given host is in IPV4
        targetName = socket.gethostbyaddr(targetIP)
        print(f"[+] The IP resolved to the following domain: {targetName[0]}")
        print(f"[+] Scan Results for: {targetName[0]}")
    except:
        print(f"[+] Scan Results for: {targetIP}")
    socket.setdefaulttimeout(3)
    # for tPort in targetPort: # This will only scan the target port given not the range
    for tPort in range(int(targetPort[0]), int(targetPort[1])+1): # This wills can all the port in the range
        t1 = threading.Thread(target=Scanner, args=(targetHost, int(tPort)))
        t1.start()


def main():
    art = pyfiglet.figlet_format("PortScanner", font="banner")
    print(art)
    print("                                                         @Author: Piyush Achärya")
    print("                                                        https://github.com/r3alix01\n")
    # Regex to check if the given IP is a valid IPV4
    ip_reg = r"\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}"
    # Regex to check iif the given domain is in the correct format
    dom_reg = r"(?:[\w]*\.)?[\w]+\.[\w]+(?:\.[\w]*)?"
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", "-H", help="Specify The Target Host to scan")
    parser.add_argument(
        '--port', "-P", help="Specify The Target Port Range to scan separated by hiphen(-)")
    if len(sys.argv) == 1:  # If no argument is specified it prints the help message along with the usage
        parser.print_help()
        parser.exit()
    args = parser.parse_args()
    if not(re.match(dom_reg, args.host) or re.match(ip_reg, args.host)):
        parser.error(
            "ERROR: Host must be in the format eg: 192.168.1.1 | www.google.com")
    ports = str(args.port).split("-")
    hosts = args.host
    portscanner(hosts, ports)


if __name__ == "__main__":
    main()
