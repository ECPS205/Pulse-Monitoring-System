import socket
from time import sleep

serverMACaddress = 'D8:3A:DD:3C:D9:91'
port = 4
data = 1
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACaddress, port))
while 1:
    s.send(bytes(str(data), 'UTF-8'))
    data = data + 1
    sleep(1)
s.close()