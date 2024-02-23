from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt(key, data):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(data,AES.block_size)
    return cipher.encrypt(padded_data)

def decrypt(key, data):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(data,)
    return unpad(decrypted_data,AES.block_size)

# Generar una clave AES
key = get_random_bytes(16)

plaintext = input("Ingrese el texto a cifrar: ").encode('utf-8')

encrypted_data = encrypt(key, plaintext)
print("Texto cifrado:", encrypted_data.hex())

decrypted_data = decrypt(key, encrypted_data)
print("Texto descifrado:", decrypted_data.decode('utf-8'))
