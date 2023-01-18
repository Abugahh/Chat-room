import binascii  # convert 1 bit to other bits
import socket  # creating sockets and binding


from pip._vendor.colorama import Fore


from CTR import _encryption
import pickle
from CTR import _decryption
message=dict
global c
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1 = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s1.bind(('localhost',2000))
s1.listen(10)  # Now wait for client connection
m=[]
c,addr=s1.accept() # Establish connection with client.
def encrypt():
    Input = input('enter message to alice: ')
    message = _encryption((Input))
    print(Fore.RED+"Ciphertext : ", binascii.hexlify(message[0]))
    m.append(message[1])
    m.append(message[2])
    data = pickle.dumps(m) #sent to alice
    c.send(message[0])  # This method transmits TCP message
    c.send(data)
    m.clear()
    message.clear()
def decrypt():
    response1 = c.recv(1024)  # This method receives TCP message
    response2 = c.recv(1024)
    resp2 = pickle.loads(response2)
    message1 = _decryption(response1, resp2[0], resp2[1])
    print(Fore.WHITE+'Reply from Alice : ', str(message1, 'utf-8'))
def loop():
    while True:
        encrypt()
        decrypt()


print(
    Fore.YELLOW + "Welcome to the chat Bob, this application is using AES-128 bit CTR Mode Algorithm for Encryption and Decryption\n"
                  "and message transmission is done using Socket Programming")

loop()
