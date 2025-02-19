import socket
import threading

# Функция для получения сообщений от сервера
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Соединение с сервером потеряно.")
            client_socket.close()
            break

# Настройка клиента
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

# Запускаем поток для получения сообщений
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

# Отправка сообщений
while True:
    message = input()
    client.send(message.encode('utf-8'))
