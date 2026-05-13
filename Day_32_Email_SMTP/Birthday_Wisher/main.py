##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random

now = dt.datetime.now()
day = now.day
month = now.month


# 1. Update the birthdays.csv
data = pandas.read_csv("./Day_32_Email_SMTP/birthday_wisher/birthdays.csv")
dic = data.to_dict(orient="records")


# 2. Check if today matches a birthday in the birthdays.csv
for i in dic:
    if i["month"] == month and i["day"] == day:
        print(i["name"])
        
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
with open(f"Day_32_Email_SMTP/birthday_wisher/letter_templates/letter_{random.randint(1,3)}.txt") as file:
    letter = file.read()
new_letter = letter.replace("[NAME]", "Masoud")
print(new_letter)

# with open(f"Day_32_Email_SMTP/birthday_wisher/letter_templates/letter_masoud.txt", "w") as file:
#     file.write(new_letter)
# print(new_letter)
# 4. Send the letter generated in step 3 to that person's email address.




