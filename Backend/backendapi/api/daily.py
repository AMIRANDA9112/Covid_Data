import requests
import datetime
import time

url = "https://covid-19-data.p.rapidapi.com/report/totals"

sd = "2020-07-21"
date = datetime.datetime.strptime(sd, '%Y-%m-%d')

for i in range(7):
    date = date - datetime.timedelta(days=1)

    date = datetime.datetime.strftime(date, '%Y-%m-%d')


    dater = date[:10]

    querystring = {"date": dater}

    headers = {
        'x-rapidapi-key': "277ae669b3msh52f0bc0d898f114p159b11jsn27bf26ae14ea",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    date = datetime.datetime.strptime(date, '%Y-%m-%d')

    time.sleep(1)
