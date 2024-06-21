import requests
import datetime as dt

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# 
# # If we don't get a 200 it will raise an exception and show the http error code
# response.raise_for_status()
# 
# # j_data = response.json()
# # print(j_data)
# j_data = response.json()['iss_position']
# longitude = j_data['longitude']
# latitude = j_data['latitude']
# iss_pos = (longitude, latitude)
# print(iss_pos)

sun_response = requests.get("https://api.sunrise-sunset.org/json?lat=29.796911468461484&lng=-98.72796144807418")
# Another way.
params = {
    "lat": "29.796911468461484",
    "lng": "-98.72796144807418",
    # Use the 24 hour clock.
    "formatted": 0,
    "tzid": "America/Mexico_City",
}
sun_response = requests.get("https://api.sunrise-sunset.org/json", params=params)
sun_response.raise_for_status()
j_data = sun_response.json()
# Just get the hour time, not the date.
sunrise = int(j_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(j_data["results"]["sunset"].split("T")[1].split(":")[0])

print(f"Sunrise is {sunrise} \nSunset is {sunset}")

now = dt.datetime.now()
# Just get the hour time, not the date.
# now = int(str(now).split(" ")[1].split(":")[0])
now = now.hour
print(now)