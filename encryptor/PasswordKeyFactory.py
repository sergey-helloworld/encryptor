import hashlib

class PasswordKeyFactory:
    @staticmethod
    def create(password):
        return hashlib.md5(password.encode()).digest()