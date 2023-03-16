import hashlib
found = 0
input_hash = input("Enter the hashed password: ")
pass_dic = input("Enter the dictionary to use: ")
try:
    pass_file = open(pass_dic, 'r')
except:
    print("ERROR")
    exit()
for word in pass_file:
    encrypted_word = word.encode("utf-8")
    hashed_word = hashlib.md5(encrypted_word.strip())
    digest = hashed_word.hexdigest()
    if digest == input_hash:
        print("PASSWORD FOUND")
        print("THE PASSWORD IS: " + word)
        found = 1
        break
if not found:
    print("PASSWORD NOT FOUND IN FILE")