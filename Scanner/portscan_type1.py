# AUTHOR: Piyush Acharya(~r3alix01)

import socket

socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET for ipv4 and socket.SOCK_STREAM for TCP
socket.setdefaulttimeout(5) # Add a timeout to 5 seconds
host = input("[+] Enter the HOST to scan: ")
port = int(input(("[+] Enter the PORT to scan: ")))

def portscan(port):
	'''Checks if connection receives to the port receives an error'''
	if socks.connect_ex((host, port)):
		print(f"port {port} is closed")
	else:
		print(f"port {port} is open")

portscan(port) 
