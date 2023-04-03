from django.shortcuts import render
import json
import requests
import urllib.request

# Create your views here.
# we are using API from:
# https://home.openweathermap.org/api_keys
#


def index(request):
    if request.method == "POST":
        city = request.POST["city"]
        latitude = 13.1
        longitude = 31.13

        url = f"https://api.meteonomiqs.com/rlknl9m9vxwh91p4/forecast/{latitude}/{longitude}/"
        headers = {
            "X-BLOBR-KEY": "7hR8HQiBEfInEwXSF1JpJWBFtp7Z0ppL"
        }

        response = requests.get(url, headers=headers)
        response_json = response.json()

        min_temp = response_json["summary"][0]["temperature"]["min"]
        max_temp = response_json["summary"][0]["temperature"]["max"]
    else:
        city = ""
        min_temp = "NaN"
        max_temp = "NaN"
    context = {"city": city, "min_temp": min_temp, "max_temp": max_temp}
    return render(request, "myweather/index.html", context)
