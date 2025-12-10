This is the socket programming assignment for ECE:3540, written by Daniel Hughes and Bashkim Useni

Instructions:
In this project you work as teams. Each team has two students.

Each student creates a client and a server. In this project we will have a TCP client/server, and a UDP client/server.

Each machine has one program running, this program acts as a client and server at the same time. One is a UDP client with a TCP server, the other is a UDP server with a TCP client.

The idea is simple:

We start by making a UDP request (the request sends a message with 3 letters).
The UDP server receives the message, then acts as a TCP client and sends a TCP request (sending the same 3 letters in revers).
The TCP server receives the message, then checks this message against what is knows to be valid messages and sends a response with values representing the ASCI of each letter after adding 41 to each letter.
If the TCP server finds the message is not valid it sends back a response with zero.
The TCP client receives the numbers, this program is also the UDP server, so it takes the numbers, adds them up, then sends the result back to the UDP client.
If the TCP client receives zero back, then the UDP server does not send a response back.
Requirements:

The UDP client sends a random 3-letter message each time it is invoked.
The TCP sever considers a message having valid letters if they have no vowels.
The UDP client must keep sending messages until a response is received.
Submission:

Please upload your code, and a video demonstrating everything is working.