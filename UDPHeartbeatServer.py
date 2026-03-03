# UDPHeartbeatServer.py
from socket import *
from time import time
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

# Assume client is dead after 5 seconds
serverSocket.settimeout(5)

while True:
    try:
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)
        msg = message.decode().split()
        sequence_num = msg[1]
        sent_time = float(msg[2])
        time_diff = time() - sent_time
        print(f"Packet {sequence_num} received. Time difference: {time_diff:.6f} s")
    except TimeoutError:
        print(f"Client stopped responding. RIP")
