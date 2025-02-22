import sqlite3

#Класс для работы с базой данных на сервере
class Db_Manager():
    def __init__(self, db_name='messenger.db'):
        self.db_name = db_name
        self._create_database()

    def _create_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
                )''')
        conn.commit()
        conn.close()    
        
    def register_user(self, username, password):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
                conn.commit()
                return True, "Регистрация успешна."
            except sqlite3.IntegrityError:
                return False, "Пользователь уже существует."

    def authenticate_user(self, username, password):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
            user = cursor.fetchone()
            return user is not None
