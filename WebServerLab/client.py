from socket import *

# Define the server's hostname and port
serverName = '172.20.10.4'
serverPort = 6789

# Create a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server
clientSocket.connect((serverName, serverPort))

# Send a GET request to the server
filename = input("Enter the filename: ").encode()
request = b'GET /' + filename + b' HTTP/1.1\r\n\r\n'
clientSocket.send(request)

# Receive the response from the server
response = b''
while True:
    data = clientSocket.recv(1024)
    if not data:
        break
    response += data

# Print the response from the server
print(response.decode())

# Close the socket
clientSocket.close()

__name__