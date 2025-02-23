import json
import pathlib

user_directory = pathlib.Path(__file__).parent.absolute()
print(user_directory)
#Функция для авторизации и регистрации, и вообще кучи всего.
def is_authorized(client):
    with open(user_directory / 'user.json', 'r') as json_file:
        data = json.load(json_file)  
        user_name = data["user_name"]
        user_password = data["user_password"]
        request = {"action": ""}
        if user_name and user_password:
            while True:
                request["action"] = "authorization"
                request["user_name"] = user_name
                request["user_password"] = user_password
                client.send(json.dumps(request).encode('utf-8'))
                message = client.recv(1024).decode('utf-8')
                response = json.loads(message)
                if response["status"] == 'success':
                    print("Вход выполнен")
                    break
                elif response["status"] == 'Error':
                    print("Попробуйте ещё раз")

        else:
            response = input("Авторизация или регистрация?(Выбирите 1 или 2)\n")
            if response == "1":
                while True:
                    request["action"] = "authorization"
                    request["user_name"] = input("Введите имя пользователья: ")
                    request["user_password"] = input("Введите пароль пользователя: ")
                    client.send(json.dumps(request).encode('utf-8'))
                    message = client.recv(1024).decode('utf-8')
                    response = json.loads(message)
                    if response["status"] == 'success':
                        user_json = {"user_name": request["user_name"],
                                     "user_password": request["user_password"]}
                        with open(user_directory / 'user.json', 'w') as json_file:
                            json.dump(user_json, json_file, ensure_ascii=False, indent=4)
                        print(response["message"])
                        print("Вход выполнен")
                        break
                    elif response["status"] == 'Error':
                        print(response["message"])
                        print("Попробуйте ещё раз")
            elif response == "2":
                while True:
                    request["action"] = "registration"
                    request["user_name"] = input("Введите имя пользователья: ")
                    request["user_password"] = input("Введите пароль пользователя: ")
                    client.send(json.dumps(request).encode('utf-8'))
                    message = client.recv(1024).decode('utf-8')
                    response = json.loads(message)
                    if response["status"] == 'success':
                        user_json = {"user_name": request["user_name"],
                                     "user_password": request["user_password"]}
                        with open(user_directory / 'user.json', 'w') as json_file:
                            json.dump(user_json, json_file, ensure_ascii=False, indent=4)
                        print(response["message"])
                        break
                    elif response["status"] == 'Error':
                        print(response["message"])
                        print("Попробуйте ещё раз")
            else:
                print("Можно вводить только 1 или 2 0_0")
