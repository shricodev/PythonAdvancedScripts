import hashlib
from os import getcwd
from platform import system
from termcolor import colored

def fileOpen(wordlist):
    global pass_file # global to use the variable outside of the function
    try:
        pass_file = open(wordlist, 'r')
    except:
        if system() == "Linux" or system() == "Darwin": # Darwin for MacOS
            print(f"[-] No Such file in the current directory: {getcwd()}/{wordlist}")
            exit(0)
        elif system() ==  "Windows":
            print(f"[-] No Such file in the current directory: {getcwd()}\{wordlist}")
            exit(0)

print("#############################################################")
print(colored("[*] Available Algorithms: md5, sha1, sha224, sha256, sha512", "cyan"))
print("#############################################################")
used_hashing = input("[+] Enter the Algorithm to Use: ").lower().strip()
user_hashes = input("[+] Enter the hash to decode: ")
wordlist = input("[+] Enter the list of password file: ")

fileOpen(wordlist)

for words in pass_file:
    if not words.strip(): # To skip the empty lines.
        continue
    else:
        print("[-] Trying " + "'" + words.strip('\n') + "'")
        encodedWord = words.encode("utf-8")
        _ = f"hashlib.{used_hashing}(encodedWord.strip()).hexdigest()"
        digests = eval(_) # eval takes the string as input and executes the content.

        if user_hashes == digests:
            print(f"[**] The decoded password is: {words}")
            exit(0)

print(f"[!!] No string matching the provided hash in the {wordlist} file")
