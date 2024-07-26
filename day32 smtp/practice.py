# import smtplib
#
#
# my_email = "dongmin001004@gmail.com"
# password = "ecgm siwn clet wfrq"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() # tls: transport layer security
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="dongmin001004@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")

import datetime as dt


now = dt.datetime.now() # -> type: datetime object
year = now.year # -> type: int
month = now.month
day = now.day
hour = now.hour

if year == 2024:
    print("We are over with covid.")

day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2000, month=10, day=4)
print(date_of_birth)