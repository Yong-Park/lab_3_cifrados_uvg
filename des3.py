from Crypto.Cipher import DES3
import random

def pad(data):
    padding_len = 8 - (len(data) % 8)
    # print("padding_len: ",padding_len)
    padding = bytes([padding_len] * padding_len)
    # print("padding: ",padding)
    return data + padding

def unpad(data):
    padding_len = data[-1]
    # print("padding_len af: ",padding_len)
    return data[:-padding_len]

def encrypt(key, data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_data = pad(data)
    # print("padded_data: ",padded_data)
    return cipher.encrypt(padded_data)

def decrypt(key, data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_data = cipher.decrypt(data)
    return unpad(decrypted_data)

key = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', k=24)).encode("utf-8")
# print(key)
plaintext = input("Ingrese el texto a cifrar: ").encode('utf-8')

encrypted_data = encrypt(key, plaintext)
print("Texto cifrado:", encrypted_data.hex())

decrypted_data = decrypt(key, encrypted_data)
print("Texto descifrado:", decrypted_data.decode('utf-8'))
