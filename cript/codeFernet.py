import base64
import os
from cryptography.fernet import Fernet

class Base64:
    def createKey(self):
        createKey = Fernet.generate_key() 
        return createKey

    def encript(self, createKey, encrypted_message):
        
 
        encryption_type = Fernet(createKey) #
        byte = str.encode(encrypted_message) #váriavel que tranforma o texto em bytes
        encrypted = encryption_type.encrypt(byte) #
        return encrypted

    ##print(encrypted_message)
    def decript(self,createKey,encrypted_message):
        encryption_type = Fernet(createKey)
        decrypted_message = encryption_type.decrypt(encrypted_message)
        
        return decrypted_message.decode()
    ##print(decrypted_message)



