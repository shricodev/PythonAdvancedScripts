#AUTHOR: Shrijal Acharya (YuShx01)

import hashlib
from requests import get

sha1hash = input("[+] Enter the SHA1 hash to decode: ")
url_content = get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt", ).text.split("\n")

for item in url_content:
    guess = hashlib.sha1(bytes(item, 'utf-8')).hexdigest()
    # print(guess)
    if guess == sha1hash:
        print(f"[+]Decoded SHA1 hash is : {item}")
        exit(1)
    else:
        print(f"[-] Password guess '{item}' doesnot match, going for next...")

print("[-] Password Not in The password list")
