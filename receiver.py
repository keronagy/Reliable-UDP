from socket import socket, AF_INET, SOCK_DGRAM
from sys import argv, stdout

from function import calculate_checksum


def send(content, to):
    checksum = calculate_checksum(content[1:])
    send_sock.sendto((checksum + content).encode("UTF-8"), to)

# serverPort = 12000
# serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# serverSocket.bind(('', serverPort))

dest_addr = 'localhost'
dest_port = 12001
dest = (dest_addr, dest_port)
listen_addr = 'localhost'
listen_port = 12000
listen = (listen_addr, listen_port)

send_sock = socket(AF_INET, SOCK_DGRAM)
recv_sock = socket(AF_INET, SOCK_DGRAM)

recv_sock.bind(listen)

expecting_seq = 0

while True:
    message, address = recv_sock.recvfrom(4096)
    message2 = message.decode("UTF-8")
    checksum = message2[:2]
    seq = message2[2]
    content = message2[3:]

    if calculate_checksum(content) == checksum:
        mes2 = content.upper();
        send(seq + mes2, dest)
        if seq == str(expecting_seq):
            print(content)
            expecting_seq = 1 - expecting_seq
    else:
        negative_seq = str(1 - expecting_seq)
        send(mes2 + negative_seq, dest)
