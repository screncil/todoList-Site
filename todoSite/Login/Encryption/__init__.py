import hashlib
import base64
import binascii
import string
import random
import uuid

class Encrypt:
    def encrypt(self, password: str):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    def generate_hash(self) -> str:
        return uuid.uuid4().hex
    