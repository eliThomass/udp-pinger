from socket import *
from time import time, sleep

clientSocket = socket(AF_INET, SOCK_DGRAM);
server_ip = '100.114.252.36'
seqNum = 0

while True:
    # Send a heartbeat every second.
    seqNum += 1
    send_time = time()
    message = f"{seqNum} {send_time}"
    clientSocket.sendto(message.encode(), (server_ip, 12000))
    print(f"Sent heartbeat {seqNum}")
    sleep(1)
