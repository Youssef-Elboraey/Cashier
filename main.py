from os import system , remove
import sqlite3
from sys import argv , platform
from colorama import Fore
#######################
def OutPutHundeler(function):

    def Hundeler(*args):

        print (f"Name\t\t\tAmount\t\t\tStatus")

        function(*args)

    return Hundeler

# def DatabaseHundeler(function):

#     def Hundeler(*args):

#         Cashier.Database = sqlite3.connect("Database/app.db")
#         Cashier.cr = Cashier.Database.cursor()

#         function(*args)

#         Cashier.Database.commit()
#         Cashier.Database.close()

#     return Hundeler

#print (str(system("pwd")).replace("0" , "") + str("/Database/app.db"))

class Cashier:

    def __init__(self , Name=None , Amount=None):

        try:

            self.Database = sqlite3.connect("/data/data/com.termux/files/home/Cashier/Database/app.db")
            self.cr = self.Database.cursor()
            self.name = str(Name).strip().capitalize()
            self.amount = Amount
            self.cr.execute("select * from Clients")
            self.clients = self.cr.fetchall()
            self.cr.execute("select * from Amounts")
            self.amounts = self.cr.fetchall()

        except IndexError:

            pass

    def save(self):

        self.Database.commit()

    def Default(self):

        if (platform == "linux"):

            system("clear")

        else:

            system("cls")

        Username = input ("Enter Username: ")

        if (Username == "Y.Elbor3y"):

#            print("Return To Defualt (It Will DELETE Database And Create It Again)!\tAre You Sure: (Yes/No)" , end="\n")

            confirm = input("Confirm: ").capitalize().strip()

            if (confirm == "Yes"):

                self.Database.close()

                remove("/data/data/com.termux/files/home/Cashier/Database/app.db")

                self.Database = sqlite3.connect("/data/data/com.termux/files/home/Cashier/Database/app.db")

                self.Database.execute("CREATE TABLE IF NOT EXISTS `Clients` ('ID' INT UNIQUE , 'Name' TEXT);")
                self.Database.execute("CREATE TABLE IF NOT EXISTS `Amounts` ('Client_ID' INT UNIQUE , 'Amount' TEXT);")

                print(Fore.LIGHTGREEN_EX + "Done")

            else:

                print(Fore.YELLOW + "Oparation CANCELED!")

        else:

            print (Fore.LIGHTRED_EX + "ACCESS DENIED")

    def add(self):

        Done = False

        if (len(self.clients) > 0):

            for client in range(len(self.clients)):

                if self.name in self.clients[client]:

                    client_id = self.clients[client][0]

                    client_amount = self.amounts[client][1] 

                    self.cr.execute(f"UPDATE Amounts SET Amount = {int(self.amount) + int(client_amount)} WHERE Client_ID = {client_id}")

                    self.save()

                    print (Fore.LIGHTGREEN_EX + "Client Has Been Updated Successfully!")

                    Done = True

                    break
        if not Done:

            self.cr.execute(f"INSERT INTO Clients VALUES ({len(self.clients) + 1} , '{self.name}')")
            self.cr.execute(f"INSERT INTO Amounts VALUES ({len(self.clients) + 1} , '{self.amount}')")

            self.save()

            print (Fore.LIGHTGREEN_EX + "Done")

    @OutPutHundeler
    def search(self):

        try:

            for client in self.clients:

                if self.name in client:

                    client_id = client[0]

                    break

            for amount in self.amounts:

                if amount[0] == client_id:

                    print(f"{client[1]}\t\t\t  {amount[1]}\t\t\tWaitting")

                    break

        except UnboundLocalError :

            print (Fore.RED + "Client\t\t\t NOT\t\t\tFOUND!")

        except :

            print (Fore.YELLOW + "Unknown Error!")

    def delete(self):

        self.name = argv[2].capitalize()

        try:

            for client in self.clients:

                if self.name == client[1]:

                    client_id = client[0]

                    break

            self.cr.execute(f"DELETE FROM Clients WHERE ID = '{client_id}'")
            self.cr.execute(f"DELETE FROM Amounts WHERE Client_ID = '{client_id}'")

        except UnboundLocalError :

            print(Fore.LIGHTBLUE_EX + "Client Already NOT In Database!")

        except :

            print (Fore.YELLOW + "Unknown Error!")

        self.save()

    @OutPutHundeler
    def showall(self):

        for client in range(len(self.clients)):

                print(f"{self.clients[client][1]}\t\t\t  {self.amounts[client][1]}\t\t\tWaitting")

try:

    Client = Cashier(argv[1] , argv[2])

except IndexError:

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
