import smtplib

# Use .env -----------------------------------------------------
import os
from dotenv import load_dotenv
load_dotenv()


# Constants ---------------------------------------------------
EMAIL = os.environ["MY_EMAIL"]
print(EMAIL)




# connection = smtplib.SMTP("smtp.gmail.com")