from os import system , remove
import sqlite3
from sys import argv
from time import sleep
#######################
def OutPutHundeler(function):

    def Decoration(*args):

        print (f"Name\t\tAmount\t\tStatus")

        function(*args)

    return Decoration

# def DatabaseHundeler(function):

#     def Hundeler(*args):

#         Cashier.Database = sqlite3.connect("Database/app.db")
#         Cashier.cr = Cashier.Database.cursor()

#         function(*args)

#         Cashier.Database.commit()
#         Cashier.Database.close()

#     return Hundeler

class Cashier:

    def __init__(self , Name=None , amount=None):

        self.Database = sqlite3.connect("Database/app.db")
        self.cr = self.Database.cursor()
        self.name = str(Name).capitalize()
        self.amount = amount
        self.cr.execute("select * from Clients")
        self.clients = self.cr.fetchall()
        self.cr.execute("select * from Amounts")
        self.amounts = self.cr.fetchall()

    def save(self):

        self.Database.commit()

    def Default(self):

        system("cls")

        print("Return To Defualt (It Will DELETE DATABASE And Create It Again)!\t(Yes/No)" , end="\n")

        sleep(2)

        confirm = input("Confirm: ").capitalize().strip()

        if (argv[2] != "Y.Elbor3y"):

            sleep(1.5)

            print("ACCESS DENIED!")

            sleep(1.5)

        elif (confirm == "Yes" and argv[2] == "Y.Elbor3y".strip()):

            self.Database.close()

            remove("Database/app.db")

            self.Database = sqlite3.connect("Database/app.db")

            self.Database.execute("CREATE TABLE IF NOT EXISTS `Clients` ('ID' INT UNIQUE , 'Name' TEXT);")
            self.Database.execute("CREATE TABLE IF NOT EXISTS `Amounts` ('Client_ID' INT UNIQUE , 'Amount' TEXT);")

            print("Done")

        else:

            print("Oparation CANCELED!")

    def add(self):

        if (len(self.clients) > 0):

            # print(len(self.clients))

            for client in self.clients:

                if self.name in client:

                    client_id = client[0]

                    self.cr.execute(f"UPDATE Amounts SET Amount = {self.amount} WHERE Client_ID = {client_id}")

                    self.save()

                    print ("Client Has Been Updated Successfully!")

                    break

                else:

                    self.cr.execute(f"INSERT INTO Clients VALUES ({len(self.clients) + 1} , '{self.name}')")
                    self.cr.execute(f"INSERT INTO Amounts VALUES ({len(self.clients) + 1} , '{self.amount}')")

                    break

        else:

            self.cr.execute(f"INSERT INTO Clients VALUES ({len(self.clients) + 1} , '{self.name}')")
            self.cr.execute(f"INSERT INTO Amounts VALUES ({len(self.clients) + 1} , '{self.amount}')")

        self.save()

    @OutPutHundeler
    def search(self):

        for client in self.clients:

            if self.name == client[1]:

                client_id = client[0]

                break

        for amount in self.amounts:

                if amount[0] == client_id:

                    print(f"{client[1]}\t\t  {amount[1]}\t\tWaitting")

                    break

    def delete(self):

        for client in self.clients:

            if self.name == client[1]:

                client_id = client[0]

                break

        self.cr.execute(f"DELETE FROM Clients WHERE ID = '{client_id}'")
        self.cr.execute(f"DELETE FROM Amounts WHERE Client_ID = '{client_id}'")

        self.save()

    @OutPutHundeler
    def showall(self):

        for client in range(len(self.clients)):

                print(f"{self.clients[client][1]}\t\t  {self.amounts[client][1]}\t\tWaitting")

if (len(argv) == 3):

    Client = Cashier(argv[1] , argv[2])

elif(len(argv) == 2):

    Client = Cashier(argv[1])

if (len(argv) > 2 and "-" not in argv[1]):

    Client.add()

elif (len (argv) == 2 and "-" not in argv[1]):

    Client.search()

elif (argv[1] == "-d"):

    Client.delete()

elif (argv[1] == "-A"):

    Client.showall()

elif (argv[1] == "-D"):

    Client.Default()
