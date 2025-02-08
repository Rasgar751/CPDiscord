import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))

server.listen(1)

print("Сервер запущен и ждёт подключений")
client, addr = server.accept()
print(f"Клиент подключился: {addr}")

data = client.recv(1024)
print(f"Клиент отправил данные: {data.decode()}")

client.send("Данные получены".encode("utf-8"))
client.close()
i = 0
while True:
    i += 1
