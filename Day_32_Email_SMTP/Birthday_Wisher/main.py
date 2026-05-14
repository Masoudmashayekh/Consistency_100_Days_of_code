##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

# Use .env ------------------------------------------------------------------------------------
import os
from dotenv import load_dotenv
load_dotenv()

# Constants -----------------------------------------------------------------------------------
MY_EMAIL = os.environ["MY_EMAIL"]
APP_PASSWORD = os.environ["APP_PASSWORD"]

# Date ----------------------------------------------------------------------------------------
today = dt.datetime.now()
day = today.day
month = today.month

# 1. Update the birthdays.csv -----------------------------------------------------------------
data = pandas.read_csv("./Day_32_Email_SMTP/birthday_wisher/birthdays.csv")
data_dict = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv ------------------------------------
for person in data_dict:
    if person["month"] == month and person["day"] == day:        
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"Day_32_Email_SMTP/birthday_wisher/letter_templates/letter_{random.randint(1,3)}.txt") as file:
            letter = file.read()
            new_letter = letter.replace("[NAME]", person["name"])
            print(new_letter)
# 4. Send the letter generated in step 3 to that person's email address. ------------------------
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= MY_EMAIL, password= APP_PASSWORD)
            connection.sendmail(
                from_addr= MY_EMAIL,
                to_addrs= person["email"],
                msg= f"Subject: Happy birthday! \n\n {new_letter}"
            )

