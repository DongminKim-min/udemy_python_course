import requests

'''response code'''
#1xx: Hold on
#2xx: Here you go
#3xx: Go away
#4xx: You screwed up
#5xx: I screwed up

response = requests.get(url="http://api.open-notify.org/iss-now.json") #<- api endpoint(location)
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

print(latitude, longitude)
