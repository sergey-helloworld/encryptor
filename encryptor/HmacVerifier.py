import hmac
import hashlib

class HmacVerifier:
    @staticmethod
    def create(key, digest):
        return hmac.new(key.encode('utf-8'), digest.encode('utf-8'), hashlib.sha256).hexdigest()

    @classmethod
    def verify(cls, key, digest, hash):
        hash_to_compare = cls.create(key, digest)
        return hash_to_compare == hash