from pymongo import MongoClient

class Connection:
    def __init__(self):
        self.uri = "mongodb+srv://josevillah:4blkAeIGFDEuO9Jr@juegozombies.se8wa.mongodb.net/?retryWrites=true&w=majority&appName=JuegoZombies"
        self.database_name = "gamez"
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.database_name]
        except Exception as e:
            print(f"An error occurred: {e}")

    def close(self):
        if self.client:
            self.client.close()
            print("Connection closed")