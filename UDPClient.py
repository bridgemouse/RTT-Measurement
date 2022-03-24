#!/usr/bin/env python3
# UDP client on localhost

from random import *
import time
import socket 
serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
outCount = 0
inCount = 0
RTTStore = []
threshold = 40
print ('\t\t\tRTT   \t\t\t\t   Threshold   \n -----------------------------\t --------------')
while outCount < 3:
    while inCount < 100:
        message = "This is a test" + str(threshold)
        message1 = message.encode('ascii')
        start = time.time()
        clientSocket.sendto(message1, (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        stop = time.time()
        RTT = stop - start
        RTTStore.append(RTT)
        inCount += 1
    def Average(arr):
        return sum(arr)/100
    RTTAve = Average(RTTStore)
    print(' ', RTTAve, ' ms', '\t\t', '   ', threshold)
    threshold += 10
    RTTStore.clear()
    inCount = 0
    outCount +=1


