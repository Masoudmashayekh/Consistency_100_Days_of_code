import requests

MY_LAT = 45.17686636485815
MY_LONG = 9.192895944384869

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}


response = requests.get("https://api.sunrise-sunset.org/json")
response.raise_for_status()