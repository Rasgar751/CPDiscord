import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))

server.listen()
print("Сервер запущен и ждёт подключений")
client, addr = server.accept()

while True:
    print(f"Клиент подключился: {addr}")
    
    message = input()
    client.send(message.encode("utf-8"))
    print(f"Клиенту отправлены данные: {message}")

    data = client.recv(1024)
    print(f"От клиента получены данные: {data.decode()}")
