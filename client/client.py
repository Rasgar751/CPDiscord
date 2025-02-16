import socket

sock = socket.socket()
sock.connect(('localhost', 12345))

while True:
    data = sock.recv(1024)
    print("От сервера получены данные: ", data.decode())

    message = input()
    print(f"Серверу отправлены данные: {message}")
    sock.send(message.encode("utf-8"))

    
