from db_manage import Db_Manager

import socket
import threading
import json

class Server():
    def __init__(self):
        self.db_manager = Db_Manager()
        self.clients = {} 
    # Функция для обработки запросов клиентов
    def handle_client(self, client_socket, addr):
        while True:
            try:
                # Получаем сообщение от клиента в формате json
                data = client_socket.recv(1024).decode('utf-8')
                request = json.loads(data)
                if not data:
                    continue
                if request["action"] == "registration":
                    username = request["user_name"] 
                    password = request["user_password"]
                    success, message = self.db_manager.register_user(username, password)
                    response = {'status': 'success' if success else 'Error', 'message': message}
                    if response['status'] == 'success':
                        self.clients[username] = client_socket 
                    client_socket.send(json.dumps(response).encode('utf-8')) 

                elif request["action"] == "authorization":
                    username = request["user_name"]
                    password = request["user_password"]
                    if self.db_manager.authenticate_user(username, password):
                        response = {'status': 'success', 'message': 'Авторизация успешна.'}
                        self.clients[username] = client_socket
                    else:
                        response = {'status': 'error', 'message': 'Неверное имя пользователя или пароль.'}
                    client_socket.send(json.dumps(response).encode('utf-8'))

                elif request["action"] == "message":
                    if request["recipient"] in self.clients:
                        self.clients[request["recipient"]].send(
                                ("\n" + request["recipient"] + ":" + request["message"]).encode('utf-8'))
                    else:
                        client_socket.send("Пользователь не в сети или не существует \n".encode('utf-8'))

            except Exception as ex:
                print("Попали в except")
                print(ex)
                continue

    #Функция запуска сервера
    def start(self):
        # Настройка сервера
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 12345))
        server.listen()

        print("Сервер запущен и ожидает подключений...")

        while True:
            client_socket, addr = server.accept()
            print(f"Подключен клиент: {addr}")
            # Запускаем поток для обработки клиента
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, addr))
            client_thread.start()

if __name__ == "__main__":
    server = Server()
    server.start()
