from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
a= "hello"
a= a.encode()
encrypt_value = f.encrypt(a)
print(encrypt_value)
print(f.decrypt(encrypt_value))
f.decrypt(encrypt_value)