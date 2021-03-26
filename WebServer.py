# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverPort = 80
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# Fill in end
print("The IP address of this server is", gethostbyname(gethostname()))
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1][1:]
        # e.g. localhost/welcome.html, message.split()[1] would be /welcome.html,
        # and filename would be welcome.html
        if not filename:
            filename = "index.html"
        f = open(filename)
        outputdata = f.read()
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send("<!DOCTYPE html>".encode())
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        print("Served", filename, "to", addr[0])
        connectionSocket.close()
    except IOError:
        outputdata = open("404NotFound.html").read()
        # Send response message for file not found
        # Fill in start
        connectionSocket.send(outputdata.encode())
        print("Served 404NotFound.html to", addr[0])
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
serverSocket.close()
exit()  # Terminate the program after sending the corresponding data
