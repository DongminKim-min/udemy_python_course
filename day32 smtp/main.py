##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
NAME = ""
def is_birthday():
    global NAME
    today = dt.datetime.today()
    this_month = today.month
    this_day = today.day

    for i in range(len(data)):
        if data.month[i] == this_month and data.day[i] == this_day:
            NAME = data.name[i]
            return True

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if is_birthday():
    message = ""
    my_email = "dongmin001004@gmail.com"
    password = "ecgm siwn clet wfrq"
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path, mode="r") as file:
        file_contents = file.read()
        message = file_contents.replace("[NAME]", NAME)
        print(message)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg= f"Subject: Happy Birthday!\n\n{message}")
        print("The letter is delivered.")

# 4. Send the letter generated in step 3 to that person's email address.




