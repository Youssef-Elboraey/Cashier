import sqlite3
from pathlib import Path

class Database:

    def __init__(self):

        self.ROOT_DIR = (str(Path(__file__).parent.resolve()) + "/../")

        self.DATABASE = self.ROOT_DIR + "Database/app.db"

        self.conn = sqlite3.connect(self.DATABASE)

        self.cursor = self.conn.cursor()

    def commit(self):

        self.conn.commit()

    def close(self):

        self.cursor.close()
        self.conn.close()
