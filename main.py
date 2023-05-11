from config.cursor import Cursor
from sys import argv
from datetime import datetime
from colorama import Fore
#######################################
class Cashier:

    def __init__(self):

        self.cursor = Cursor()
        self.date = f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}"
        self.is_exists = True if self.get_id() != None else False

    def get_id(self , Name: str = argv[1]):

        try:

            return int(self.cursor.select(["id"] , "Clients" , f"Name = '{Name.capitalize()}'")[0][0])

        except IndexError:
 
            return None

    def get_operations(self):

        Operations = self.cursor.select(["id" , "Operation" , "Amount" , "Date"] , "Operations" , f"client_id = {self.get_id()}")

        if not Operations:

            return None

        return Operations
    
    def add(self , Name: str , Operation: str , Amount: int):

        Name = Name.capitalize()

        if not self.is_exists:

            self.cursor.insert("Clients" , {"Name" : Name})
            self.cursor.insert("Clients_ids" , {"Name" : Name})
        
        self.cursor.insert("Operations" , {"client_id" : self.get_id() , "Operation" : Operation , "Amount" : Amount , "Date" : self.date})
        self.cursor.insert("History" , {"client_id" : self.get_id() , "Operation" : Operation , "Amount" : Amount , "Date" : self.date})

        print (Fore.LIGHTGREEN_EX + "Done" + Fore.RESET)

    def search(self):

        if not self.is_exists:

            return (Fore.LIGHTRED_EX + "Client Not Exists" + Fore.RESET)

        elif self.get_operations() != None: 

            self.show(data=self.get_operations())

        else:

            return f"{argv[1]} Has No Operations"

        return ""
    
    def delete(self , Operation_id: int , Amount: int):

        amount = self.cursor.select(["Amount"] , "Operations" , f"`id` = {Operation_id}")[0]

        if not amount:

            exit(Fore.LIGHTRED_EX + "Operation Not Exists!" + Fore.RESET)

        if (amount[0] - int(Amount)) == 0:

            self.cursor.delete("Operations" , f"id = {Operation_id}")

        else:

            self.cursor.custom(f"UPDATE `Operations` SET Amount = Amount - {Amount} WHERE `id` = {Operation_id}")

        print(Fore.LIGHTGREEN_EX + "Done" + Fore.RESET)

    def get_all(self):

        clients = self.cursor.select(["*"] , "Clients")

        for client in clients:

            self.show(Clients=[client[1]] , data=self.cursor.select(["id" , "Operation" , "Amount" , "Date"] , "Operations" , f"client_id = '{client[0]}'"))

    def show(self , Clients: str = [argv[1]] , data: list = []):

        total_of_amounts: int = 0

        for client in Clients:

            print(f"{client.capitalize()}:")
        
            for id , operation , amount , date in data:
                
                total_of_amounts += amount

                print (f"    ID: {id}\n    Operation: {operation}\n    Amount: {amount}\n    Date: {date}\n")
        
        print(f"Total Of Amounts Is: {total_of_amounts}\n")

cashier = Cashier()

if len(argv) == 4:

    cashier.add(argv[1] , argv[2] , argv[3])

elif len(argv) == 2:

    if "-A" in argv:

        cashier.get_all()

    else:

        print(cashier.search())

elif len(argv) == 5:

    cashier.delete(argv[3] , argv[4])
