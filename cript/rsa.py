from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class Rsa:
    def __init__(self):
        self.keyPair = RSA.generate(3072)

    def createPublicKey(self):
        pubKey = self.keyPair.publickey()
        return pubKey

    def createPrivateKey(self):
        privKeyPEM = self.keyPair.exportKey()
        return privKeyPEM

    def encript(self, msg, pubKey):
        encryptor = PKCS1_OAEP.new(pubKey)
        encrypted = encryptor.encrypt(msg)
        return encrypted

    def decript(self, encrypted,privkey):
        decryptor = PKCS1_OAEP.new(self.keyPair)
        decrypted = decryptor.decrypt(encrypted)
        return decrypted
        