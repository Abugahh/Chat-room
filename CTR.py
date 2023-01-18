import os      # to interact w the operating system
import pbkdf2    # password based key derivation function
import pyaes
import secrets   # used for generating random numbers for managing important data such as passwords




def _encryption(p):
    password = "s3cr3t*c0d3"
    passwordSalt = os.urandom(16)
    key = pbkdf2.PBKDF2(password, passwordSalt).read(16)  # generates a key for encyption

    m=[]
    m.clear()
    iv = secrets.randbits(128)
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))  # counter progcess changes the initialization vector
    ciphertext = aes.encrypt(p)
    m.append(ciphertext),m.append(key),m.append(iv)
    return m

def _decryption(c,k,iv):
    aes = pyaes.AESModeOfOperationCTR(k, pyaes.Counter(iv))
    decrypted = aes.decrypt(c)
    return decrypted

# the opposite of encryption the key ,iv we get aes and with a predefined function called decrypt in
# pyaes module we decrypt the ciphertext which is saved and retured