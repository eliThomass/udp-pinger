from socket import *
from time import clock_gettime_ns, CLOCK_MONOTONIC, time

clientSocket = socket(AF_INET, SOCK_DGRAM);
clientSocket.settimeout(1)

server_ip = '100.114.252.36' 

minRTT = float('inf')
maxRTT = float('-inf')
avgRTT = 0
numPackets = 10
numLost = 0


for i in range(numPackets):
    sendTime = clock_gettime_ns(CLOCK_MONOTONIC)
    message = f"Ping {i + 1} {time()}"
    clientSocket.sendto(message.encode(), (server_ip, 12000))
    try:
        response = clientSocket.recv(1024).decode()
        responseTime = clock_gettime_ns(CLOCK_MONOTONIC)
        RTT = (responseTime - sendTime) / 1e9
        if RTT < minRTT or RTT > maxRTT:
            minRTT = min(minRTT, RTT)
            maxRTT = max(maxRTT, RTT)
        if numPackets > numLost:
            avgRTT /= (numPackets - numLost)
        else:
            avgRTT = 0
        print(f"Response: {response}\nRTT: {RTT:.6f} s")
    except TimeoutError:
        numLost += 1
        print("Request timed out")
    print("\n")

avgRTT /= (numPackets - numLost)

print(f"-------------Ping Stats for {server_ip}-------------")
print(f"Packet Loss: {numLost / numPackets * 100}%")
print(f"RTT min/avg/max : {minRTT:.6f}/{avgRTT:.6f}/{maxRTT:.6f} s")

