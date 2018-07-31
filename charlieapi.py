
import requests


def get_data():
    ship_api_url = "https://app.uhds.oregonstate.edu/api/webcam/ship"
    request_data = requests.get(ship_api_url)
    return request_data.json()

data = get_data()
print(data)
