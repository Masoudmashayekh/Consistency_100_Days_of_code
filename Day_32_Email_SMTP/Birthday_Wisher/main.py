import os
import dotenv
import smtplib
from dotenv import load_dotenv
load_dotenv()
EMAIL = os.environ["MY_EMAIL"]
print(EMAIL)
# connection = smtplib.SMTP("smtp.gmail.com")