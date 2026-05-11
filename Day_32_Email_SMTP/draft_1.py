# Day 32: Email SMTP and the datetime module
# Simple Mail Transfer Protocol


# import smtplib

# # Use .env -----------------------------------------------------
# import os
# from dotenv import load_dotenv
# load_dotenv()


# # Constants ---------------------------------------------------
# MY_EMAIL = os.environ["MY_EMAIL"]
# APP_PASSWORD = os.environ["APP_PASSWORD"]
# CLIENT_EMAIL = os.environ["CLIENT_EMAIL"]
# # SMTP -------------------------------------------------------
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  # For security reasion
#     connection.login(user= MY_EMAIL, password= APP_PASSWORD)
#     connection.sendmail(
#         from_addr= MY_EMAIL, 
#         to_addrs= CLIENT_EMAIL, 
#         msg="Subject: Hello \n\n This is body of my email."
#         )


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
hour = now.hour
print(now)
print(year)
print(month)
print(day)
print(day_of_week)

print(hour)
