import socket
import threading

# Функция для обработки подключений клиентов
def handle_client(client_socket, addr):
    while True:
        try:
            # Получаем сообщение от клиента
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                continue
            print(f"Получено сообщение: {message}")
            # Пересылаем сообщение всем клиентам
            for client in clients:
                client.send(f"Пользователь {addr} отправил сообщение: {message} ".encode('utf-8'))
        except Exception as ex:
            print("Попали в except")
            print(ex)
            continue

# Настройка сервера
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen()

print("Сервер запущен и ожидает подключений...")

clients = []

while True:
    client_socket, addr = server.accept()
    print(f"Подключен клиент: {addr}")
    clients.append(client_socket)
    # Запускаем поток для обработки клиента
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
