
from codeFernet import Base64
from rsa import Rsa
import time
import binascii


while True:
    base6 = Base64()
    rsa = Rsa()
    #msg = input("Mensagem a ser cifrada: ")
    criarkey = base6.createKey()
    keyPublic = rsa.createPublicKey()
    keyPrivate = rsa.createPrivateKey()
  

    controller = input("Digite '0' para finalizar: \nDigite '1' criptografia simétrica para assimétrica e ver todos os passos: \nDigite '2' para criptografar somente para Base64: \nDigite '3' para decriptografar Base64: ")
    if controller == '0':
        break
    elif controller == '1':
        msg = input("Mensagem a ser criptografada: ")
        start = time.time()
        encriptar = base6.encript(criarkey, msg)
        encriptBase64ForRSA = rsa.encript(encriptar, keyPublic)
        decriptBase64ForRSA = rsa.decript(encriptBase64ForRSA, keyPrivate.upper())
        decriptar = base6.decript(criarkey, encriptar)
        finish = time.time()
        print ("criador de chave", criarkey)
        print ("Mensagem criptografada:", encriptar)
        print ("Mensagem criptografada base64 para criptografia RSA:", encriptBase64ForRSA )
        print ("funcionando?", decriptBase64ForRSA)
        print ("Mensagem decriptografada:",decriptar)
        print ("tempo de execução: ", finish - start, " ms")
    elif controller == '2':
        msg = input("Mensagem a ser criptografada: ")
        start = time.time()
        criarkey = base6.createKey()
        encriptar = base6.encript(criarkey, msg)
        finish = time.time()
        print ("Sua chave para decriptografia é: ", criarkey.decode())
        print ("Sua mensagem encriptografada  é: ", encriptar.decode())
        print ("tempo de execução: ", finish - start, " ms")
    elif controller == '3':
        keyDecript = input("Informe sua chave para decriptografar: ")
        msgDecript = input("Informe sua mensagem para decriptografia: ")
        start = time.time()
        decriptarBase64 = base6.decript(keyDecript.encode(), msgDecript.encode())
        finish = time.time()
        print ("Sua mensagem decriptografada é: ", decriptarBase64)
        print ("tempo de execução: ", finish - start, " ms")
   
