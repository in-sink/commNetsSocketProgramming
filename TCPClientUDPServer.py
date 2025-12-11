#boilerplate code taken from ch2 lecture slides
from socket import *

#helper function to add the TCPinputs back and add the values up
def tallyInput(input):
    #splits into each number seperately
    inputs = input.split(',')
    output = 0
    for i in inputs:
        output += int(i)

    return output

#main function for running TCPClientUDPServer, does everything sequentially, no multithreading is required
def main():
    #port information
    serverPort = 1200
    tcpServerName = 'localhost'
    tcpServerPort = 12001
    print('UDP Server listening on port 1200')
    print('The server is ready to receive')
    serverSocket = socket(AF_INET,SOCK_DGRAM)
    serverSocket.bind(("", serverPort))    

    #creating the tcp socket
    tcpSocket = socket(AF_INET, SOCK_STREAM)
    tcpSocket.connect((tcpServerName, tcpServerPort))
    tcpSocket.settimeout(3)

    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        message = message.decode()
        print(f'Received from UDP Client: {message}')
        
        # Reverse the message
        reversed_message = message[::-1]
        print(f'Reversed: {reversed_message}')

        # Create TCP socket and send reversed message to TCP Server
        try:
            tcpSocket.send(reversed_message.encode())
            print(f'Sent via TCP to TCP Server: {reversed_message}')
            print(f"Waiting for TCP response")

            #waits for a response back from the TCPServer
            tcpResponse = tcpSocket.recv(1024)

            #if the response isn't a 0, send the UDP response
            if tcpResponse.decode() != "0":
                serverSocket.sendto(tallyInput(tcpResponse.decode()).encode(), clientAddress)
            else:
                break
        except timeout:
            print(f"No response received for {message}")
            
        except Exception as e:
            print(f'Error connecting to TCP Server: {e}')

    serverSocket.close()
    tcpSocket.close()

if __name__ == "__main__":
    main()