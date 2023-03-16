import hashlib
text = input("ENTER THE TEXT TO ENCRYPT: ")
hash_obj = hashlib.md5(text.encode())
result = hash_obj.hexdigest()
print(result)