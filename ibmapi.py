import requests
from databaseGUI import *
import json

gui = Gui()
classNum = gui.startLoop()

def get_data():
    api_url = "http://192.168.200.115:10208//web/services/RTVITEMSVCCGREST/itemclass/" + classNum
    request_data = requests.get(api_url, headers={"Accept":"application/json"})
    return request_data

    
data = get_data()
print(data.json())

with open("data_file.json", "w") as write_file:
    json.dump(data.json(), write_file)