from socket import *
from time import clock_gettime_ns, CLOCK_MONOTONIC
from datetime import datetime

clientSocket = socket(AF_INET, SOCK_DGRAM);
clientSocket.settimeout(1)

server_ip = '100.96.11.84'

minRTT = float('inf')
maxRTT = float('-inf')
avgRTT = 0
numPackets = 10
numLost = 0


for i in range(numPackets):
    sendTime = clock_gettime_ns(CLOCK_MONOTONIC)
    message = f"Ping {i + 1} {datetime.now()}"
    clientSocket.sendto(message.encode(), (server_ip, 12000))
    try:
        response = clientSocket.recv(1024).decode()
        responseTime = clock_gettime_ns(CLOCK_MONOTONIC)
        RTT = (responseTime - sendTime) / 1e6
        if RTT < minRTT or RTT > maxRTT:
            minRTT = min(minRTT, RTT)
            maxRTT = max(maxRTT, RTT)
        avgRTT += RTT
        print(f"Response: {response}\nRTT: {RTT:.6f} ms")
    except TimeoutError:
        numLost += 1
        print("Request timed out")
    print("\n")

avgRTT /= numPackets

print(f"-------------Ping Stats for {server_ip}-------------")
print(f"Packet Loss: {numLost / numPackets * 100}%")
print(f"RTT min/avg/max : {minRTT:.3f}/{avgRTT:.3f}/{maxRTT:.3f} ms")

