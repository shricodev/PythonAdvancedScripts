import hashlib
from os import getcwd
from platform import system

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

md5hash = input("[+] Enter the md5 hash to decode: ")
wordlist = input("[+] Enter the list of password file: ")

fileOpen(wordlist)

for words in pass_file:
    if not words.strip(): # To skip the empty lines.
        continue
    else:
        print("[-] Trying " + "'" + words.strip('\n') + "'")
        encodedWord = words.encode("utf-8")
        md5digests = hashlib.md5(encodedWord.strip()).hexdigest()

        if md5hash == md5digests:
            print(f"[**] The decoded password is: {words}")
            exit(0)

print(f"[!!] No string matching the provided hash in the {wordlist} file")
