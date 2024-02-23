from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image

def encrypt_cbc(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return iv, ciphertext

def decrypt_cbc(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)
    return unpad(decrypted_data, AES.block_size)

def encrypt_ecb(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def decrypt_ecb(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    return unpad(decrypted_data, AES.block_size)

# Cargar imágenes
foto1 = Image.open("img/foto1.jpeg")
logo = Image.open("img/Logo-UVG.webp")
tux = Image.open("img/tux.ppm")

# Convertir imágenes a bytes
foto1_bytes = foto1.tobytes()
logo_bytes = logo.tobytes()
tux_bytes = tux.tobytes()

# Generar una clave AES
key = get_random_bytes(16)

# Modo CBC
# Encriptar imágenes
iv_foto1, encrypted_foto1 = encrypt_cbc(key, foto1_bytes)
iv_logo, encrypted_logo = encrypt_cbc(key, logo_bytes)  # ECB se utiliza solo para demostración, no se recomienda para imágenes
iv_tux, encrypted_tux = encrypt_cbc(key, tux_bytes)    # ECB se utiliza solo para demostración, no se recomienda para imágenes

# Guardar imágenes encriptadas
with open("result/cbc/encrypt_cbc_foto1.jpeg", "wb") as f:
    f.write(encrypted_foto1)
with open("result/cbc/encrypt_cbc_logo.webp", "wb") as f:
    f.write(encrypted_logo)
with open("result/cbc/encrypt_cbc_tux.ppm", "wb") as f:
    f.write(encrypted_tux)

# Desencriptar imágenes
decrypted_foto1 = decrypt_cbc(key, iv_foto1, encrypted_foto1)
decrypted_logo = decrypt_cbc(key,iv_logo, encrypted_logo)
decrypted_tux = decrypt_cbc(key,iv_tux, encrypted_tux)

# Crear imágenes desde los bytes desencriptados
decrypted_foto1_img = Image.frombytes(foto1.mode, foto1.size, decrypted_foto1)
decrypted_logo_img = Image.frombytes(logo.mode, logo.size, decrypted_logo)
decrypted_tux_img = Image.frombytes(tux.mode, tux.size, decrypted_tux)

# Guardar imágenes desencriptadas
decrypted_foto1_img.save("result/cbc/decrypt_cbc_foto1.jpeg")
decrypted_logo_img.save("result/cbc/decrypt_cbc_logo.webp")
decrypted_tux_img.save("result/cbc/decrypt_cbc_tux.ppm")


# Modo ECB
# Encriptar imágenes
encrypted_foto1 = encrypt_ecb(key, foto1_bytes)
encrypted_logo = encrypt_ecb(key, logo_bytes)  # ECB se utiliza solo para demostración, no se recomienda para imágenes
encrypted_tux = encrypt_ecb(key, tux_bytes)    # ECB se utiliza solo para demostración, no se recomienda para imágenes

# Guardar imágenes encriptadas
with open("result/ecb/encrypt_ecb_foto1.jpeg", "wb") as f:
    f.write(encrypted_foto1)
with open("result/ecb/encrypt_ecb_logo.webp", "wb") as f:
    f.write(encrypted_logo)
with open("result/ecb/encrypt_ecb_tux.ppm", "wb") as f:
    f.write(encrypted_tux)

# Desencriptar imágenes
decrypted_foto1 = decrypt_ecb(key, encrypted_foto1)
decrypted_logo = decrypt_ecb(key, encrypted_logo)
decrypted_tux = decrypt_ecb(key, encrypted_tux)

# Crear imágenes desde los bytes desencriptados
decrypted_foto1_img = Image.frombytes(foto1.mode, foto1.size, decrypted_foto1)
decrypted_logo_img = Image.frombytes(logo.mode, logo.size, decrypted_logo)
decrypted_tux_img = Image.frombytes(tux.mode, tux.size, decrypted_tux)

# Guardar imágenes desencriptadas
decrypted_foto1_img.save("result/ecb/decrypt_ecb_foto1.jpeg")
decrypted_logo_img.save("result/ecb/decrypt_ecb_logo.webp")
decrypted_tux_img.save("result/ecb/decrypt_ecb_tux.ppm")