import socket

def grabber(ip, port):
    try:
        socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)
        socks.connect((ip,port))
        banner = socks.recv(1024)
        return banner
    except:
        return ""

def main():
    ip = input("[+] Enter the IPv4 to scan: ")
    lower_range = int(input("[+] Enter the lower range port: "))
    upper_range = int(input("[+] Enter the upper range port: "))
    for port in range(lower_range, upper_range+1):
        banner = grabber(ip, port)
        if banner:
            print(f"[*] {ip}/{port}: {banner}")

if __name__ == "__main__":
    main()
