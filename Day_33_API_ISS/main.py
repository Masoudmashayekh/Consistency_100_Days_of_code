import requests
from datetime import datetime



# Constants --------------------------------------------------------------
MY_LAT = 45.176792
MY_LONG = 9.192834

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

# API ISS-------------------------------------------------------------------
response = requests.get(url= "http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()["iss_position"]

longitude = float(data["longitude"])
latitude = float(data["latitude"])

iss_position = (longitude, latitude)
# https://www.latlong.net/

print(iss_position)    

# API Sun-------------------------------------------------------------------
response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0] # 2026-05-17T03:49:34+00:00
sunset = data["results"]["sunset"].split("T")[1].split(":")[0] # 2026-05-17T03:49:34+00:00

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)