import datetime
import logging
import azure.functions as func

import requests
from twilio.rest import Client

def rain ():
    api_key = ""
    parameters = {
        "lat": -33.872761,
        "lon": 151.205338,
        "exclude": "current,minute,daily",
        "appid": api_key
    }

    account_sid = ""
    auth_token = ""

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
    
    print("code works")


def main(mytimer: func.TimerRequest) -> None:

    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    rain()
    
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
