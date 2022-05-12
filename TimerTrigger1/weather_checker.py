import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

def rain()-> str:
    api_key = "f76aaa1d50a0166a5bf5b7693136611f"
    parameters = {
        "lat": -33.872761,
        "lon": 151.205338,
        "exclude": "current,minute,daily",
        "appid": api_key
    }

    account_sid = "ACbd18305fe11649d61fce28d4634f50ec"
    auth_token = "c9be1e77d76a35ebb8c4ddfce7ebd380"

    response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    response.raise_for_status()
    weather_data = response.json()

    hourly_weather_slice = weather_data["hourly"][0:13]

    will_rain = False

    for hour in hourly_weather_slice:
        condition_code = hour["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True

    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="Bring an umbrella today, it's going to rain. 🌧",
            from_='+18312730625',
            to='+61431220867'
        )

        return message.status
    else:
        return "No Rain"