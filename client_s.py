import socket  # for sockets
import sys  # for exit

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

host = '192.168.1.11';
port = 8888;

while 1:
    msg = input('Enter message to send : ')

    try:
        # Set the whole string
        s.sendto(msg.encode(), (host, port))

        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print('Server reply : ' + reply.decode("utf-8"))

    except socket.error as msg:
        print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()