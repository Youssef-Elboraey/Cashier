import urllib
from json import loads
from pathlib import Path
from os import popen
MainPath = str(Path(__file__).parent.resolve())

with open(MainPath + "/JSON/Infos.json") as infos:

    data = loads(infos.read())


file = urllib.urlopen("https://github.com/Youssef-Elboraey/Cashier/blob/main/JSON/Infos.json")

with open(file) as f:

    new_data = loads(f.read())


my_version = str(data["APP"]["Version"])

new_version = str(new_data["APP"]["Version"])

if (my_version != new_version):

    popen("rm -rf ~/Cashier && git clone https://www.github.com/Youssef-Elboraey/Cashier.git")
