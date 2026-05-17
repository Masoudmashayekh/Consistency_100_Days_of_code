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
def is_iss_overhead():
    response = requests.get(url= "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()["iss_position"]

    iss_longitude = float(data["longitude"])
    iss_latitude = float(data["latitude"])

    iss_position = (iss_longitude, iss_latitude)
    # https://www.latlong.net/

    print(iss_position)
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    
    
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

