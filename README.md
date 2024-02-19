# IPv4-fragmentation
The project aims to demonstrate IPv4
fragmentation using a client-server
architecture. The client program will accept a
file with text data and the Maximum
Transmission Unit (MTU) size from the user.
It will then fragment the data based on the
MTU size and send the packets to the server.
The server will receive the fragmented
packets, reassemble the datagram, and display
the original data.Along with that we will get fragmented data in our file as different text files.



Client Side Code Summary:
The client program (client.py) performs the
following steps:
1. Imports the socket module for network
communication.
2. Defines the fragment_and_send_data()
function, which takes the file path and
MTU size as input.
3. Creates a socket object (client_socket)
using socket.socket().
4. Connects to the server using the
connect() method with the server's
address and port.
5. Opens the specified file in read mode
and reads the data.
6. Fragments the data into smaller chunks
based on the MTU size.
7. Sends each fragment to the server using
sendall() method of the socket.
8. Closes the socket connection.


Server Side Code Summary:
The server program (server.py) performs the
following steps:
1. Imports the socket module for network
communication.
2. Defines the receive_and_reassemble_data()
function.
3. Creates a socket object (server_socket)
using socket.socket().
4. Binds the server socket to a specific
address and port using bind() method.
5. Listens for incoming connections using
listen() method.
6. Accepts incoming connection from the
client using accept() method, which
returns a new socket object
(client_socket) and the client's address.
7. Receives data fragments from the client
using the recv() method in a loop until
no more data is received.
8. Reassembles the fragments into the
original data.
9. Prints information about each received
fragment.
10.Prints the reassembled data.
11. Closes the client and server sockets.
