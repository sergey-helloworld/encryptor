#!/usr/bin/python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from .EndsWithIVCipherDataPreparer import EndsWithIVCipherDataPreparer
from system import singleton
import os

@singleton
class Encryptor:
	IV_LEN = 16
	IV_STORE_MODE_MANUAL = 1
	IV_STORE_MODE_EOF = 2

	def __init__(self, iv_store_mode = IV_STORE_MODE_MANUAL):
		if iv_store_mode == self.IV_STORE_MODE_EOF:
			self.preparer = EndsWithIVCipherDataPreparer()
		else:
			self.preparer = None

	def encrypt(self, key, message, iv = None):
		if iv is None:
			iv = os.urandom(16)
		e_obj = AES.new(key, AES.MODE_CBC, iv)
		encoded_str = e_obj.encrypt(pad(message, 16))
		if self.preparer is not None:
			return self.preparer.join(encoded_str, iv)
		else:
			return encoded_str

	def decrypt(self, key, message, iv = None):
		if self.preparer is not None:
			prepared = self.preparer.split(message, self.IV_LEN)
			iv = prepared['iv']
			message = prepared['body']
		d_obj = AES.new(key, AES.MODE_CBC, iv)
		return unpad(d_obj.decrypt(message), 16)
