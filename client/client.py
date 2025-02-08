import socket
sock = socket.socket()
sock.connect(('localhost', 12345))
sock.send('hello world!'.encode("utf-8"))

data = sock.recv(1024)
sock.close()

print(data.decode())
