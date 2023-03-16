import hashlib
text = input("ENTER THE TEXT TO ENCRYPT: ")
hash_obj = hashlib.sha256(text.encode())
result = hash_obj.hexdigest()
print(result)