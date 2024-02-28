from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from PIL import Image
import io

def decrypt_ecb(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    return unpad(decrypted_data, AES.block_size)

def decrypt_cbc(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)
    return unpad(decrypted_data, AES.block_size)

# Clave hexadecimal
key_hex = "406845db899854cc23484d6f3f28f3f7"

# Convertir la clave hexadecimal a binario
key_binary = bytes.fromhex(key_hex)

# Modo ECB
encrypted_foto1_path = "lab3_ejercicio/mr-increible_encrypted_image.jpeg"
# Leer la imagen cifrada como un archivo binario
with open(encrypted_foto1_path, "rb") as file:
    encrypted_data = file.read()

# Desencriptar imágenes
decrypted_data = decrypt_ecb(key_binary, encrypted_data)

# Crear un objeto Image desde los bytes desencriptados
decrypted_image = Image.open(io.BytesIO(decrypted_data))

# Obtener las dimensiones de la imagen desencriptada
decrypted_image_size = decrypted_image.size

# Guardar imágenes desencriptadas
decrypted_image.save("resultados_parte1/mr-increible.jpeg")
