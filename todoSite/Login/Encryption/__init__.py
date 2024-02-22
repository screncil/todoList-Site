import hashlib
import base64
import binascii
import string
import random

class PasswordEncrypt:
    def encrypt(self, password: str):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()