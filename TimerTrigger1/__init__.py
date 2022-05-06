import datetime
import logging
import TimerTrigger1.weather_checker as weather_checker

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    message = weather_checker.rain
    print (message)
    return message

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
