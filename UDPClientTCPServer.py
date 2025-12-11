#Initial code taken from ch2 slides
from socket import *
from concurrent.futures import ThreadPoolExecutor, as_completed #for multithreading
import random
import string

#port information
UDPClientName = 'localhost'
UDPClientPort = 1200
TCPServerName = 'localhost'
TCPServerPort = 12000
TCPClientName = 'localhost'
TCPClientPort = 12001


#helper function to generate a random 3 letter code to send to the UDP server
def generateMessage():
    message = ""
    for x in range(3):
        message = message + (random.choice(string.ascii_uppercase))
    return message

#helper function to parse the information sent from the UDPServer
#returns a string containing the number to send back to TCPClient
def parseMessage(message, validMessages):

    #get reversed messsage, and ensures it is in validMessages
    if message[::-1] in validMessages :

        #if there is a vowel, return 0
        for c in message:
            if c in ['A','E','I','O','U']:
                return 0
            
        #building the output
        output = ""
        for c in message:
            num = ord(c) - 65
            if num < 10:
               output += "0" + str(num)
            else:
               output += str(num)
            #add a comma after each number
            output += ","
        return output
    
    #if there isn't a valid input 
    else:
        return 0


#helper funciton to send the UDP message
def sendUDPMessage(sentMessages):
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    
    #one second timeout, so it resends the data if nothing is receieved back.
    clientSocket.settimeout(1)

    #generating the message, and appending to known messages array
    message = generateMessage()
    sentMessages.append(message)

    #sending
    clientSocket.sendto(message.encode(), (UDPClientName,UDPClientPort))

    #console output
    print(f"Sent {message} to {UDPClientName} at port {UDPClientPort}")
    print("Valid Messages:")
    for sentMessage in sentMessages:
        print('\t' + sentMessage)

    #Waits 1s for a response, if not sends another
    while True:
        try:
            data, addr = clientSocket.recvfrom(1024)
            message = data.decode()
            break

        except timeout:
            #if no response, regenerate a new message, add to sent messages, and print
            print(f"No response for {message}")
            message = generateMessage()
            sentMessages.append(message)
            clientSocket.sendto(message.encode(),((UDPClientName, UDPClientPort)))
            print(f"Sent {message} to {UDPClientName} at port {UDPClientPort}")
            print("Valid Messages:")
            for sentMessage in sentMessages:
                print('\t' + sentMessage)

    clientSocket.close()
    #prints to console when the UDP response is receieved.
    print(f"Response from UDP server receieved with {message}")


#helper function to recveive the TCP message
def recvTCPMessage(messagesSent):
    #initiating TCP connection
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', TCPClientPort))
    serverSocket.listen(1)
    print(f"Listening at {TCPServerName}, port {TCPServerPort}")
    print(f"Received ")

    while True:
        #receieves the message
        connectionSocket, addr = serverSocket.accept()
        data, addr = connectionSocket.recv(1024)
        message = data.decode().upper()

        #calls the helper function to figure out what to send to the TCP client
        output = parseMessage(message, messagesSent)

        #sends back the decoded message such that a = 01, b = 02, c = 03 etc.
        connectionSocket.send(output.encode())

        connectionSocket.close()
        
        if output != "0":
            # stop listening after sending a non-zero response
            break

def main():
    messagesSent = []

    with ThreadPoolExecutor(max_workers=2) as executor:
        tcp_task = executor.submit(recvTCPMessage, messagesSent)
        udp_task = executor.submit(sendUDPMessage, messagesSent)

if __name__ == "__main__":
    main()
