from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


def generate_aes_key():
    """Genera una clave AES de 256 bits y un IV de 128 bits"""
    key = os.urandom(32)  
    iv = os.urandom(16)   
    return key, iv


def encrypt_with_aes(key, iv, message):
    """Cifra un mensaje usando AES en modo CBC"""
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    # Padding para asegurar que el mensaje sea múltiplo de 16
    padded_message = message.ljust((len(message) + 15) // 16 * 16).encode('utf-8')
    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()
    return encrypted_message

# Descifra un mensaje usando AES en modo CBC
def decrypt_with_aes(key, iv, encrypted_message):
    """Descifra un mensaje usando AES en modo CBC"""
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()
    return decrypted_message.decode('utf-8').strip()  

# Servicio de encriptación
def service_encript(text):
    """Genera la clave, el IV y cifra el texto proporcionado"""
    key, iv = generate_aes_key()
    encrypted_message = encrypt_with_aes(key, iv, text)
    return key, iv, encrypted_message
