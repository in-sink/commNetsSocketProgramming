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

#helper function to parse the information sent from the UDPServer
#returns a string containing the number to send back to TCPClient
def parseMessage(message, validMessages):
    
    return message

#port information
UDPClientName = 'localhost'
UDPClientPort = 1200
TCPServerName = 'localhost'
TCPServerPort = 12000

#helper funciton to send the UDP message
def sendUDPMessage(sentMessages):
    clientSocket = socket(AF_INET,SOCK_DGRAM)

    #generating the message, and appending to known messages array
    message = generateMessage()
    sentMessages.append(message)

    #sending
    clientSocket.sendto(message.encode(), (UDPClientName,UDPClientPort))
    clientSocket.close()

    #console output
    print(f"Sent {message} to {UDPClientName} at port {UDPClientPort}")
    print("Valid Messages:")
    for sentMessage in sentMessages:
        print('\t' + sentMessage)

#helper function to recveive the TCP message
def recvTCPMessage():
    #initiating TCP connection
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', UDPClientPort))
    serverSocket.listen(1)
    print(f"Listening at {TCPServerName}, port {TCPServerPort}")
    print(f"Received ")

    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        connectionSocket.send(sentence.encode())
        connectionSocket.close()



#Create the initial array of valid messages
messagesSent = []
sendUDPMessage(messagesSent)
