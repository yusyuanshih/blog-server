from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from app.config import Config


AES_KEY = Config.AES_KEY.encode()


def encrypt(plaintext: str) -> bytes:
    cipher = AES.new(AES_KEY, AES.MODE_CBC)
    padded_text = pad(plaintext.encode(), AES.block_size)
    return cipher.iv, cipher.encrypt(padded_text)


def decrypt(iv: bytes, ciphertext: bytes) -> str:
    cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    return unpad(decrypted_padded_text, AES.block_size).decode()
