from config.cursor import Cursor
from datetime import datetime
################################
class Operations:

    def __init__(self):

        self.cursor = Cursor()
        self.cursor.DB = None

    def add(self):

        pass

    def inqury(self):

        pass

    def delete(self):

        pass

class Safe(Operations):

    def __init__(self):
        super().__init__()
        self.cursor.DB = self.cursor.ROOT_DIR + "Database/safe.db"
        self.cursor.connect()
        self.date = f"{datetime.now().year}-{datetime.now().month}-"

    def add(self , Day , Amount):

        self.cursor.insert("Cash" , {"Date" : self.date + str(Day) , "Amount" : Amount})
    
    def inqury(self):

        amounts = self.cursor.select(["Amount"] , "Cash")

        return sum([amount[0] for amount in amounts])
    
    def delete(self , Day , Amount):

        self.cursor.insert("Cash" , {"Date" : self.date + str(Day) , "Amount" : -Amount})


safe = Safe()

# safe.add(16 , 1000)
print (safe.inqury())
# safe.delete(16 , 70)