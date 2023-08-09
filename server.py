from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
PORT_NUMBER = 5001
SIZE = 1024

hostName = gethostbyname('0.0.0.0')

mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind((hostName, PORT_NUMBER))

print("Test server listening on port {0}\n".format(PORT_NUMBER))

while True:
    (data, addr) = mySocket.recvfrom(SIZE)
    print(data)