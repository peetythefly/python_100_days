import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
S_EMAIL = "sandboxofpatrick@gmail.com"
S_PASS = "crtmeahoyxtznpoj"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
lat_diff = abs(MY_LAT - iss_latitude)
lng_diff = abs(MY_LONG - iss_longitude)
print(lat_diff)
print(lng_diff)
if (time_now.hour >= sunset or time_now.hour <= sunrise) and lat_diff <= 5 and lng_diff <= 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(S_EMAIL, S_PASS)
        connection.sendmail(from_addr=S_EMAIL,
                            to_addrs=S_EMAIL,
                            msg="Look up. It's the ISS Satellite!\n\nThis message brought to you by your python code on day 33."
                            )

