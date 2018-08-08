import requests
from databaseGUI import *
import json

#Initializes the main loop for the GUI which takes text input
gui = Gui()
classNum = gui.startLoop()

#Calls the IBM i API with whichever number was input, adds a JSON header, and returns the data as JSON
def get_data():
    api_url = "http://192.168.200.115:10208//web/services/RTVITEMSVCCGREST/itemclass/" + classNum
    request_data = requests.get(api_url, headers={"Accept":"application/json"})
    return request_data

    
data = get_data()
print(data.json())

#Creates a json file, "w" means you can write to it, and json.dump writes the JSON result to the file
with open("data_file.json", "w") as write_file:
    json.dump(data.json(), write_file)
