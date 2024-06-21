import requests
import auth
from twilio.rest import Client


lat = auth.lat
lon = auth.lon
api_key = auth.weather_api_key 
# We only want weather for the next 12 hours. Since we are getting weather data every 3 hours we only need a count of 4.
cnt = 4
units = "imperial"
url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units={units}&cnt={cnt}"


raw_response = requests.get(url)
raw_response.raise_for_status()
raw_weather = raw_response.json()
weather_3_hr_intval = raw_weather["list"]
will_rain = False
# If a weather id is less than 700, it will rain.
for interval in weather_3_hr_intval:
    weather_id = interval["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    # print("It's going to rain in the next 12 hours.")

    # Use twilio for WhatsApp messaging.
    account_sid = auth.twilio_sid
    auth_token = '[AuthToken]'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_=f'whatsapp:+{auth.twilio_phone}',
      body="It's going to rain in the next 12 hours",
      to=f'whatsapp:+{auth.phone_number}'
    )

    print(message.sid)


# SMS doesn't work with twilio anymore.