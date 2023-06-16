from .database import Database

class Cursor(Database):

    def insert(self , table: str , data: dict):

        columns = ','.join(data.keys())
        values = ','.join([f'"{value}"' for value in data.values()])

        self.cursor.execute(f"INSERT INTO `{table}` ({columns}) VALUES ({values});")

        self.commit()
        self.close()

    def update(self , table: str , data: dict , condition: str = "1 = 1"):

        for column , value in data.items():

            self.cursor.execute(f"UPDATE `{table}` SET {column} = '{value}' WHERE {condition};")

        self.commit()
        self.close()

    def delete(self , table: str , condition: str = "1 = 1"):
        
        self.cursor.execute(f"DELETE FROM {table} WHERE {condition};")

        self.commit()
        self.close()

    def select(self , record: list , table: str , condition: str = "1 = 1"):

        columns = ",".join(record)

        self.cursor.execute(f"SELECT {columns} FROM {table} WHERE {condition};")

        return self.cursor.fetchall()

    def custom(self , query: str):

        self.cursor.execute(query)

        self.commit()
        self.close()
