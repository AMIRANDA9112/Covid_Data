import requests
import json


data = json.load(open('country.json', 'r'))

url = "https://covid-19-data.p.rapidapi.com/country/code"

for l in data:

    code = l.get("name")

    if code == "Argentina":

        querystring = {"code": l.get("alpha2code")}
        headers = {
            'x-rapidapi-key': "277ae669b3msh52f0bc0d898f114p159b11jsn27bf26ae14ea",
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)











