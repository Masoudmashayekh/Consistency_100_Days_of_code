import smtplib

# Use .env -----------------------------------------------------
import os
from dotenv import load_dotenv
load_dotenv()


# Constants ---------------------------------------------------
EMAIL = os.environ["MY_EMAIL"]

# SMTP -------------------------------------------------------
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()  # For security resion
connection.login(user= EMAIL, password=)