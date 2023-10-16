import socket
import bluetooth

hostMACAddress = 'D8:3A:DD:3C:D9:91' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 4 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
try:
    print("Opening socket")
    client, address = s.accept()
    print(address)
    while 1:
        data = client.recv(size)
        if data:
            print(data.decode('UTF-8'))
        client.send(data)
except:
    print("Closing socket")	
    client.close()
    s.close()