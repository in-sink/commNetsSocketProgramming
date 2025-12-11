#boilerplate code taken from ch2 lecture slides
from socket import *

#helper function to add the TCPinputs back and add the values up
def tallyInput(input):
    #splits into each number seperately
    inputs = input.split()
    output = 0
    for i in inputs:
        #skips empty split for trailing comma
        if i != '': 
            output += int(i)

    return str(output)

#main function for running TCPClientUDPServer, does everything sequentially, no multithreading is required
def main():
    #port information
    UDP_SERVER_PORT = 1200
    tcpServerName = 'localhost'
    tcpServerPort = 12000
    print(f'UDP Server listening on port {UDP_SERVER_PORT}')
    print('The server is ready to receive')
    serverSocket = socket(AF_INET,SOCK_DGRAM)
    serverSocket.bind(("", UDP_SERVER_PORT))    

    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        message = message.decode()
        print(f'Received from UDP Client: {message}')
        
        # Reverse the message
        reversed_message = message[::-1]
        print(f'Reversed: {reversed_message}')

        # Create TCP socket and send reversed message to TCP Server
        try:
            with socket(AF_INET, SOCK_STREAM) as tcpSocket:
                tcpSocket.settimeout(3)
                tcpSocket.connect((tcpServerName, tcpServerPort))
                tcpSocket.send(reversed_message.encode())
                print(f'Sent via TCP to TCP Server: {reversed_message}')
                print(f"Waiting for TCP response")

                tcpResponse = tcpSocket.recv(1024)
                decoded = tcpResponse.decode()
                print(f"Received {decoded} from TCP Server")

                if decoded != "0":
                    response = tallyInput(decoded)
                    print(f"Sending {response} to UDP client")
                    serverSocket.sendto(response.encode(), clientAddress)
                else:
                    break
        except timeout:
            print(f"No response received for {message}")
            
        except Exception as e:
            print(f'Error connecting to TCP Server: {e}')

    serverSocket.close()

if __name__ == "__main__":
    main()
