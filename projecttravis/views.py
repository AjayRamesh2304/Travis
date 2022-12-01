from django.shortcuts import render
import requests
import json

def home(request):
    return render(request, 'index.html')

def iccstats(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

    querystring = {"formatType":"test"}

    headers = {
    "X-RapidAPI-Key": "ddf0d0319cmsh58ccbfa13a818e9p157a52jsn9ef1654fef2a",
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    iccdata = json.loads(response.text)
    listiccdata = []
    iccstandings = {}
    rank = []
    name = []
    d = iccdata["rank"]
    print(d)
    for i in d:
        rank.append(i["rank"])
        name.append(i["name"])
    return render(request, 'icc.html', {'name': name, 'rank': rank})
      
     