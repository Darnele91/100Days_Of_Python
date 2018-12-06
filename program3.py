import hashlib
checksum=0
a_string = "12 32 15 25"
for letter in a_string:
    checksum = (checksum + (32*ord(letter)+12)) % 255

print(checksum)
with open(__file__,"rb") as f:
    print(hashlib.md5(f.read()).hexdigest())
