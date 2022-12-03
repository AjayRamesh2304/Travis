from django.shortcuts import render
import requests
import json
from django.views import View
from django.http import HttpResponse

class RequestStandings(View):
    
    def get(self, request):
        url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

        querystring = {"formatType":"t20"}

        headers = {
        "X-RapidAPI-Key": "ddf0d0319cmsh58ccbfa13a818e9p157a52jsn9ef1654fef2a",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
        }
        
        response = requests.request("GET", url, headers=headers, params=querystring)
        iccdata = json.loads(response.text)
        name = []
        d = iccdata["rank"]
        for i in d:
            name.append(i["name"])
        return render(request, 'icc.html', {'name': name})
        