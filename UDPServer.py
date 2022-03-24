# !/usr/bin/env python3
# UDP  server on localhost
import time
from socket import *
from random import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    message1 = message.decode('ascii')
    size = len(message1)
    threshold = message1[(size-2):size]
    message2 = message1[:-2]
    for i in range(10):
        a = randrange(0, 100, 5)
    if a > int(threshold):
        time.sleep(2)
        modifiedMessage = message2.upper().encode('ascii')
        serverSocket.sendto(modifiedMessage, clientAddress)
    elif a <= int(threshold):
        modifiedMessage = message2.upper().encode('ascii')
        serverSocket.sendto(modifiedMessage, clientAddress)
