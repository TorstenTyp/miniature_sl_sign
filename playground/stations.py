import requests

URL = 'https://transport.integration.sl.se/v1/sites?expand=false'
headers = {
    "Content-Type": "application/json" 
}

response = requests.get(URL, headers=headers)

for station in response.json():
    print(station['name'] + ": " + str(station['id']))
