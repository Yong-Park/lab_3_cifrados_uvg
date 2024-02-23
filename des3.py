from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt(key, data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_data = pad(data,DES3.block_size)
    # print("padded_data: ",padded_data)
    return cipher.encrypt(padded_data)

def decrypt(key, data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_data = cipher.decrypt(data)
    return unpad(decrypted_data,DES3.block_size)

key = key = get_random_bytes(24)
# print(key)
plaintext = input("Ingrese el texto a cifrar: ").encode('utf-8')

encrypted_data = encrypt(key, plaintext)
print("Texto cifrado:", encrypted_data.hex())

decrypted_data = decrypt(key, encrypted_data)
print("Texto descifrado:", decrypted_data.decode('utf-8'))
