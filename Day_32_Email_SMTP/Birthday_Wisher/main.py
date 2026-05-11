import smtplib

# Use .env -----------------------------------------------------
import os
from dotenv import load_dotenv
load_dotenv()


# Constants ---------------------------------------------------
MY_EMAIL = os.environ["MY_EMAIL"]
APP_PASSWORD = os.environ["APP_PASSWORD"]
CLIENT_EMAIL = os.environ["CLIENT_EMAIL"]
# SMTP -------------------------------------------------------
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()  # For security reasion
connection.login(user= MY_EMAIL, password= APP_PASSWORD)
connection.sendmail(
    from_addr= MY_EMAIL, 
    to_addrs= CLIENT_EMAIL, 
    msg="Subject: Hello \n\n This is body of my email."
    )
connection.close()