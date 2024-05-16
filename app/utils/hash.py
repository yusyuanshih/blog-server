from hashlib import sha256


def get_hash(text: bytes | str) -> str:
    if isinstance(text, str):
        text = text.encode("utf-8")
    return sha256(text).digest()
