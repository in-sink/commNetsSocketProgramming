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

