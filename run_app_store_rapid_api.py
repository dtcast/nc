import requests

url = "https://app-stores.p.rapidapi.com/reviews"

querystring = {"store": "apple", "id":"1517783697","language":"ko"}

headers = {
    "X-RapidAPI-Key": "14c64cc381msheeb66906c0fd3a1p11cda7jsnd840bd01c5a8",
    "X-RapidAPI-Host": "app-stores.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)