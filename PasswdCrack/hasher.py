import hashlib

hashval = input("[+] Enter the string to hash: ")

hash_object1 = hashlib.md5()
hash_object1.update(hashval.encode())
print(f"MD5 hash is: {hash_object1.hexdigest()}") # HEXDIGEST IS STHE MAIN FUNCTION THAT IS RETURNING THE AHSH OF THE GIVEN STRING

hash_object2 = hashlib.sha1()
hash_object2.update(hashval.encode())
print(f"SHA1 hash is: {hash_object2.hexdigest()}")

hash_object3 = hashlib.sha224()
hash_object3.update(hashval.encode())
print(f"SHA224 hash is: {hash_object3.hexdigest()}")

hash_object4 = hashlib.sha256()
hash_object4.update(hashval.encode())
print(f"SHA256 hash is: {hash_object4.hexdigest()}")

hash_object5 = hashlib.sha512()
hash_object5.update(hashval.encode())
print(f"SHA512 hash is: {hash_object5.hexdigest()}")