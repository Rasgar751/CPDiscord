from autrisation import is_authorized

import json
import socket
import threading

class Client():
    # Функция для получения сообщений от сервера
    def receive_messages(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    continue
                else:
                    print(message)
            except:
                print("Соединение с сервером потеряно.")
                client_socket.close()
                break

    def start(self):
        # Настройка клиента
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Для применения на локальной машине
        # server.bind(('127.0.0.1', 1234))
        client.connect(('185.185.69.218', 5555))

        is_authorized(client)

        # Запускаем поток для получения сообщений
        receive_thread = threading.Thread(target=self.receive_messages, args=(client,))
        receive_thread.start()

        # Отправка сообщений
        while True:
            data = {"action": "message", 
                    "recipient": input("Введите имя пользователя которому вы хотите отправить сообщение: "),
                    "message": input("Введите сообщение: ")}
            client.send(json.dumps(data).encode('utf-8'))

if __name__ == "__main__":
    client = Client()
    client.start()
