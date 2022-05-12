import traceback

import rsa
import logging
import base64

logger = logging.getLogger(__name__)


class Encryptor:
    def __init__(self):
        self.__decryption_private_key_path = 'keys/decryption-private-key.pem'
        self.__encryption_public_key_path = 'keys/encryption-public-key.pem'

    def decrypt(self, ciphertext):
        return self.__decrypt(ciphertext)

    def encrypt(self, plaintext):
        return self.__encrypt(plaintext)

    def __decrypt(self, ciphertext):
        key = self.__load_private_key(self.__decryption_private_key_path)

        try:
            return rsa.decrypt(ciphertext, key).decode('utf-8')
        except Exception as e:
            return False

    def __encrypt(self, plaintext):
        key = self.__load_public_key(self.__encryption_public_key_path)

        try:
            encrypted = rsa.encrypt(plaintext.encode('utf-8'), key)
            encoded = base64.b64encode(encrypted)
            return encoded.decode('utf-8')
        except Exception as e:
            traceback.print_exc()
            print(e)
            return False

        pass

    def __load_private_key(self, key_path):
        with open(key_path, 'rb') as file:
            rsa_key = rsa.PrivateKey.load_pkcs1(file.read())

        return rsa_key

    def __load_public_key(self, key_path):
        with open(key_path, 'rb') as file:
            rsa_key = rsa.PublicKey.load_pkcs1_openssl_pem(file.read())

        return rsa_key
