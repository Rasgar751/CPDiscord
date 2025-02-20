import socket
import threading
import json


def is_authorized():
    """Проверяет авторизован ли пользователь, 
    если нет предоставляет выбор: зарегестироваться или авторизоватся,
    сдесь же регистрируется или авторизуется.(Возможно функция немного перегруженна 0_0 )"""
    with open('user.json', 'r', encoding='utf-8') as file:
        data = json.load(file)  
        print(data)

# Функция для получения сообщений от сервера
def receive_messages(client_socket):
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

is_authorized()

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
