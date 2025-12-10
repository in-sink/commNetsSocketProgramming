#boilerplate code taken from ch2 lecture slides
#UDP Server - Receives 3-letter string from UDP Client, reverses it, sends via TCP to TCP Server

from socket import *

serverPort = 1200
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print('UDP Server listening on port 1200')
print('The server is ready to receive')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    received_message = message.decode()
    print(f'Received from UDP Client: {received_message}')
    
    # Reverse the message
    reversed_message = received_message[::-1]
    print(f'Reversed: {reversed_message}')
    
    # Create TCP socket and send reversed message to TCP Server
    tcpServerName = 'localhost'
    tcpServerPort = 12000
    
    try:
        tcpSocket = socket(AF_INET, SOCK_STREAM)
        tcpSocket.connect((tcpServerName, tcpServerPort))
        tcpSocket.send(reversed_message.encode())
        print(f'Sent via TCP to TCP Server: {reversed_message}')
        tcpSocket.close()
    except Exception as e:
        print(f'Error connecting to TCP Server: {e}')
