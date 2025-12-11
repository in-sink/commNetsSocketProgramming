#boilerplate code taken from ch2 lecture slides
from socket import *

# TCP connection to server
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.sent(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())

# Receive three numbers from TCP server
numbers_data = clientSocket.recv(1024).decode()
print('Received from TCP Server:', numbers_data)

#  UDP server details
udpServerName = 'localhost'
udpServerPort = 1200

# Parse and sum the three numbers
try:
    numbers = list(map(float, numbers_data.split()))
    if len(numbers) != 3:
        print('Error: Expected 3 numbers')
    else:
        total = sum(numbers)
        print(f'Sum of {numbers}: {total}')
        
        # Only send UDP response if sum is not 0
        if total != 0:
            # Create UDP socket and send result to UDP server
            udpSocket = socket(AF_INET, SOCK_DGRAM)
            message = str(total)
            udpSocket.sendto(message.encode(), (udpServerName, udpServerPort))
            print(f'Sent sum {total} via UDP to server')
            udpSocket.close()
        else:
            print('Sum is 0 - no UDP response sent')
except ValueError:
    print('Error: Could not parse numbers')

clientSocket.close()



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