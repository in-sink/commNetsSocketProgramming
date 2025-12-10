#Initial code taken from ch2 slides
from socket import *
import random
import string

#helper function to generate a random 3 letter code to send to the UDP server
def generateMessage():
    message = ""
    for x in range(3):
        message = message + (random.choice(string.ascii_lowercase))
    return message

#port information
serverName = 'localhost'
serverPort = 12000

#helper funciton to send the UDP message
def sendUDPMessage():
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    message = generateMessage()
    clientSocket.sendto(message.encode(), (serverName,serverPort))
    clientSocket.close()
    print(f"Sent {message} to {serverName} at port {serverPort}")

#helper function to recveive the TCP message
def recvTCPMessage():
    print(f"Received ")

sendUDPMessage()

#TCP Server code
#boilerplate code from ch2 ppt

from socket import *
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())

    connectionSocket.close()