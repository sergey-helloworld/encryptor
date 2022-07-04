from encryptor import HmacVerifier


hash = HmacVerifier.create('helllo', 'test message')
print(HmacVerifier.verify('helllo', 'test message', hash))