import hashlib
password = input("Enter The Password")
password = hashlib.sha256(password.encode('utf-8')).hexdigest()
print(password)