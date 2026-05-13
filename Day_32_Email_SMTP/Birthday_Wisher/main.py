##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt

now = dt.datetime.now()
day = now.day
month = now.month
print(month)

# 1. Update the birthdays.csv
data = pandas.read_csv("./Day_32_Email_SMTP/birthday_wisher/birthdays.csv")
dic = data.to_dict(orient="records")
for i in dic:
    if i["month"] == month and i["day"] == day:
        print(i["name"])

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




