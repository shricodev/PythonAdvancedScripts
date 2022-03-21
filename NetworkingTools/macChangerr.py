from termcolor import colored
import subprocess


def changeAddress(interface, mac_addr):
    '''
    This function runs all the linux command to turn down
    and change the mac address on the interface provided by the user.
    '''
    subprocess.call(["ifconfig " + interface + "down"])
    subprocess.call(["ifconfig" + interface + "hw" + "ether" + mac_addr]) # This is the line responsible for mac address change
    subprocess.call(["ifconfig" + interface + "up"])


def main():
    print(colored("This Script Is Applicable to Only LINUX Users, Windows Users Get Lost!\n", 'cyan'))
    interface = input("[+] Enter The Interface To Change The MAC Address: \n")
    new_mac = input("[+] Enter The New MAC Address To Change To: \n")
    prev_mac_address = subprocess.check_output(["ifconfig " + interface])
    changeAddress(interface, new_mac)
    after_mac_addr = subprocess.check_output(["ifconfig " + interface])

    if prev_mac_address == after_mac_addr:
        print(colored("[-] Failed To Change Mac Address!", "red"))
    else:
        print(
            f"[>>] Successfully changed the MAC Address to: {new_mac} on {interface}")


if __name__ == "__main__":
    main()
