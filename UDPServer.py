#boilerplate code taken from chapter 2 slides

from socket import *

serverPort = 1200
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print('The server is receive')

while true:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
