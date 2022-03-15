import socket
import sys
import re
import threading
import argparse

def main():
	ip_reg = r"\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}" # Regex to check if the given IP is a valid IPV4
	dom_reg = r"(?:[\w]*\.)?[\w]+\.[\w]+(?:\.[\w]*)?" # Regex to check iif the given domain is in the orrect format
	parser = argparse.ArgumentParser()
	parser.add_argument("--host", "-H", help="Specify The Target Host to scan")
	parser.add_argument('--port', "-P", help="Specify The Target Port to scan separated by comma")
	if len(sys.argv)==1: # If no arhument is specified it prints the help message along with the usage
		parser.print_help()
		parser.exit()
	args = parser.parse_args()
	if not(re.match(dom_reg, args.host) or re.match(ip_reg, args.host)):
		parser.error("ERROR: Host must be in the format eg: 192.168.1.1 | www.google.com")
	ports = str(args.port).split(",")
	print(ports)

if __name__ == "__main__":
	main()