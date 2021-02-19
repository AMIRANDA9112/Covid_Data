import requests
import json
import datetime
import time

day = datetime.datetime.now()

data = json.load(open('country.json', 'r'))

url = "https://covid-19-data.p.rapidapi.com/report/country/code"

c = 0

for m in data:

    code = m.get("name")

    if code == "Afghanistan":

        for l in data:
            day = datetime.datetime.strftime(day, '%Y-%m-%d')
            querystring = {"date": day[:10], "code": m.get("alpha2code")}

            headers = {
                'x-rapidapi-key': "277ae669b3msh52f0bc0d898f114p159b11jsn27bf26ae14ea",
                'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)

            day = datetime.datetime.strptime(day, '%Y-%m-%d')

            day = day - datetime.timedelta(days=1)

            time.sleep(1)

            c += 1

            if c == 7:
                break

            else:
                pass

        break

    else:
        pass
