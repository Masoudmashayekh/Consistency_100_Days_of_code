import requests
from datetime import datetime
import smtplib
import time

# Use .env ------------------------------------------------------------------------------------
import os
from dotenv import load_dotenv
load_dotenv()

# Constants -----------------------------------------------------------------------------------
MY_EMAIL = os.environ["MY_EMAIL"]
APP_PASSWORD = os.environ["APP_PASSWORD"]
CLIENT_EMAIL = os.environ["CLIENT_EMAIL"]
MY_LAT = 45.176792
MY_LONG = 9.192834


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
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0] # 2026-05-17T03:49:34+00:00
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0] # 2026-05-17T03:49:34+00:00
    print(sunrise)
    print(sunset)

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True



# -------------------------------
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user= MY_EMAIL, password= APP_PASSWORD)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs= CLIENT_EMAIL,
            msg= "Subject: Look Up 👆🏻\n\n The ISS is above you in the sky."
        )
        