# AUTHOR: Piyush Acharya(~r3alix01)

import socket
from termcolor import colored

socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET for ipv4 and socket.SOCK_STREAM for TCP
socket.setdefaulttimeout(3) # Add a timeout to 3 seconds
host = input("[+] Enter the HOST to scan: ")
lower_range = int(input("[+] Enter the lower range port: "))
upper_range = int(input("[+] Enter the upper range port: "))

def portscan(port):
	'''Checks if connection receives to the port receives an error'''
	if socks.connect_ex((host, port)):
		print(colored(f'[!]Port {port} is closed', 'red'))
	else:
		print(colored(f'[!]Port {port} is open', 'green'))

for port in range(lower_range, upper_range+1): # Scans the specified ports
	portscan(port) 
