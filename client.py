from socket import socket, AF_INET, SOCK_DGRAM

SERVER_IP = 'IP of the receiver'
PORT_NUMBER = 5000
SIZE = 1024
print("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket(AF_INET, SOCK_DGRAM)
while True:
    myMessage = input("Message: ")
    person = " sender> "
    myMessage = (person + myMessage)
    mySocket.sendto(myMessage.encode('utf-8'), (SERVER_IP, PORT_NUMBER))
