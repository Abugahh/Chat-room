import pickle  # converting an object in memory to a byte stream that can be stored on disk or sent over a network.
import socket
import binascii

from pip._vendor.colorama import Fore   # Colorama is a module to color the python outputs


from CTR import _encryption
from CTR import _decryption
message1=[]
m=[]
s2 = socket.socket() # Create a socket object
s2.bind(('172.20.10.2',2001))  # Bind its own address to the port
s2.connect(('172.20.10.3',2000))

def encrypt():
    Input = input('enter message to bob :')
    message1 = _encryption((Input))
    print(Fore.RED+"Ciphertext : ",binascii.hexlify(message1[0]))
    m.append(message1[1])
    m.append(message1[2])
    data = pickle.dumps(m)  # sends to bob
    s2.send(message1[0])
    s2.send(data)
def decrypt():
    m.clear()
    message1.clear()
    response1 = s2.recv(1024)    # key and iv are received
    response2 = s2.recv(1024)
    resp2 = pickle.loads(response2)     # loading the info w help of pickle to send to CTR mode
    message = _decryption(response1, resp2[0], resp2[1])     # sending key saved in resp 1,iv and ciphertext to decryption
    print(Fore.WHITE+'Message from Bob : ', str(message, 'utf-8'))     # decrypted message obtained here
def loop():
    while True:
        decrypt()
        encrypt()
print(Fore.YELLOW+ "Welcome to the chat Alice, this application is using AES-128 bit CTR Mode Algorithm for Encryption and Decryption\n"
                  "and message transmission is done using Socket Programming")
loop()