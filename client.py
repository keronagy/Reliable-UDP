import socket
from socket import timeout
from function import calculate_checksum

serverName = 'localhost'
serverPort = 12000
clientName = 'localhost'
clientPort = 12001

clientSendSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM )

clientReceiveSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

clientReceiveSocket.bind((clientName,clientPort))
clientReceiveSocket.settimeout(1) #raises a timeout exception if 1.5 seconds has elapsed before client receives from server
packetNumber=0

while 1:

    packet = input('Input lowercase sentence:')
    ackisReceived = False

    while not ackisReceived: #keep resending packet until server sends acknowledgment for the packet and checksum comparison succeeds
        clientSendSocket.sendto( (calculate_checksum(packet) + str(packetNumber) + packet).encode('UTF-8'), (serverName, serverPort))  #concatenate checksum of packet with packetNumber and Packet Data and send to server

        try:
            message2, address = clientReceiveSocket.recvfrom(4096)
        except timeout:
            print('timeout occurred')
        else:
            # print(message)
            # checksum = message[:2]
            # acknowledged_packetNumber = message[5]
            # if calculate_checksum(message[2:]) == checksum and acknowledged_packetNumber == str(packetNumber):
            #     ack_received = True
            message = message2.decode("UTF-8")
            checksum = message[:2]
            acknowledged_packetNumber = message[2]
            print (message[3:])
            n = calculate_checksum(message[3:])
            if calculate_checksum(message[3:]) == checksum and acknowledged_packetNumber == str(packetNumber):
                ackisReceived = True

    if packetNumber ==1:
        packetNumber =0
    else:
        packetNumber =1


