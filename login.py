from connection import Connection
class Login:
    def __init__(self):
        self.conn = Connection()
        self.conn.connect()
        self.db = self.conn.db

    def login(self, data):
        users = self.db.users.find()
        for user in users:
            print(user)  # Imprime cada documento encontrado

        self.conn.close()  # Cierra la conexión