from socket import *
import threading

# Function to handle requests
def handle_request(connectionSocket):
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputData = f.read()
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
        for i in range(0, len(outputData)):
            connectionSocket.send(outputData[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
        connectionSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
PORT = 6789
serverSocket.bind(('', PORT))
serverSocket.listen(5)
print('The web server is up on port:', PORT)

while True:
    print("Ready to server...")
    connectionSocket, address = serverSocket.accept()
    t = threading.Thread(target=handle_request, args=(connectionSocket,))
    t.start()