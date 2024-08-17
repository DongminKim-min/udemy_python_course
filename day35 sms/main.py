import requests
from twilio.rest import Client

END_POINT = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "175d4b02f1acb0478b55f189d2d22a49"
account_sid = "AC4b2125af66e06da78324e3c107b726b2"
auth_token = "d6fcf9661e6055c01d47cd1aa9f7f3d7"

params = {
    "lat": 37.5,
    "lon": 127,
    "cnt": 12,
    "appid": api_key
}

response = requests.get(url=END_POINT, params=params)
response.raise_for_status()
weather_data = response.json()["hourly"][:12]
weather_id_list = [data["weather"][0]["id"] for data in weather_data]
print(weather_id_list)

will_rain = False
for i in weather_id_list:
    if i < 700:
        will_rain = True

if will_rain:
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an umbrella!☔",
            from_='whatsapp:+14155238886',
            to = 'whatsapp:+491739708177'
        )
        print(f"Message sent successfully: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")

else:
    print("No rain expected. No message sent.")
