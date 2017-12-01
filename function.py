# thx to xhacker
#reference https://github.com/xhacker/RDT-over-UDP/blob/master/common.py

import socket,sys

def calculate_checksum(data):  # Form the standard IP-suite checksum
    pos = len(data)
    if (pos & 1):  # If odd...
        pos -= 1
        sum = ord(data[pos])  # Prime the sum with the odd end byte
    else:
        sum = 0

    # Main code: loop to calculate the checksum
    while pos > 0:
        pos -= 2
        sum += (ord(data[pos + 1]) << 8) + ord(data[pos])

    sum = (sum >> 16) + (sum & 0xffff)
    sum += (sum >> 16)

    result = (~ sum) & 0xffff  # Keep lower 16 bits
    result = result >> 8 | ((result & 0xff) << 8)  # Swap bytes
    p0 =(result / 256)
    p1=(int)(result / 256)
    p2 = chr((int)(result / 256))
    p3= (result % 256)
    p4= chr(result % 256)
    n=  p2+p4
    return n