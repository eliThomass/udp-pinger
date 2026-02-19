from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM);

for i in range(10):
    message = f"Ping number: {i}"
    clientSocket.sendto(message.encode(), ("127.0.0.1", 12000))

