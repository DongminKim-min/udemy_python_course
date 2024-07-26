import smtplib
import datetime as dt
import random
def is_friday():
    now = dt.datetime.now()
    day_of_week = now.weekday()
    if day_of_week == 4:
        return True

if is_friday():
    with open(file="quotes.txt", mode="r", encoding="utf-8") as file:
        quote_list = file.readlines()
        today_quote = random.choice(quote_list)

    my_email = "dongmin001004@gmail.com"
    password = "ecgm siwn clet wfrq"

    message = f"Subject: Quote of Today\n\n{today_quote}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=message.encode("utf-8"))
        print("A quote of today is sent.")

