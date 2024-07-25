import smtplib
import requests
from datetime import datetime
import time

MY_EMAIL = "dave012284@gmail.com"
MY_PASSWORD = "Dave1004@"
MY_LAT = 52.108273
MY_LNG = 9.362171


def is_iss_overhead():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_data = iss_response.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    if (abs(MY_LAT - iss_lat) <= 5) & (abs(MY_LNG - iss_lng) <= 5):
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    time_now = datetime.now()

    if (time_now.hour >= sunset_hour) or time_now.hour <= sunrise_hour:
        return True


while True:
    if is_iss_overhead() and is_dark():
        # connection = smtplib.SMTP("")
        # connection.starttls()
        # connection.login(MY_EMAIL, MY_PASSWORD)
        # connection.sendmail(
        #     from_addr=MY_EMAIL,
        #     to_addrs=MY_EMAIL,
        #     msg="Subject:Look UP \n\nThe ISS is above you in the sky."
        # )
        print("Look up. It is above you in the sky.")
    else:
        print("Not yet.")
    time.sleep(10)


