from socket import *
from time import clock_gettime_ns, CLOCK_MONOTONIC

clientSocket = socket(AF_INET, SOCK_DGRAM);
clientSocket.settimeout(1)


for i in range(10):
    sendTime = clock_gettime_ns(CLOCK_MONOTONIC)
    message = f"Ping {i + 1} {sendTime}"
    clientSocket.sendto(message.encode(), ("100.114.252.36", 12000))
    try:
        response = clientSocket.recv(1024).decode()
        responseTime = clock_gettime_ns(CLOCK_MONOTONIC)
        RTT = (responseTime - sendTime) / 1e9
        print(f"Response: {response}\nRTT: {RTT:.6f} sec")
    except TimeoutError:
        print("Request timed out")
    print("\n")

print("---------------------------")
