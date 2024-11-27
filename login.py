from connection import Connection
import bcrypt
class Login:
    def __init__(self):
        self.conn = Connection()
        self.conn.connect()
        self.db = self.conn.db

    def login(self, data):
        user = self.db.users.find_one({
            "username": data["username"]},
            {"password":1}
        )

        # Si el usuario existe
        if user:
            # Convertir la contraseña ingresada a bytes
            entered_password = data['password'].encode('utf-8')
            
            # Comparar la contraseña ingresada con el hash almacenado
            if bcrypt.checkpw(entered_password, user['password'].encode('utf-8')):
                userData = self.db.users.find_one({
                    "username": data["username"]},
                    {"_id": 1, "username":1, "email":1, "role":1}
                )
                return userData  # Contraseña válida, retornar el usuario
            else:
                return False  # Contraseña incorrecta
        else:
            return False  # Usuario no encontrado
        
