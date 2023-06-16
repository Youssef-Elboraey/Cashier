import sqlite3
from pathlib import Path

class Database:

    ROOT_DIR = (str(Path(__file__).parent.resolve()) + "/../")

    def __init__(self):    

        self.DB = None

        self.connection = None

        self.cursor = None

    def connect(self):

        self.connection = sqlite3.connect(self.DB)

        self.cursor = self.connection.cursor()

    def commit(self):

        self.connection.commit()

    def close(self):

        self.cursor.close()
        self.connection.close()
