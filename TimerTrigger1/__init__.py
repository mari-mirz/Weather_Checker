import datetime
import logging
<<<<<<< HEAD
from weather_checker import rain

=======
from main import rain
>>>>>>> 6eec79cd7bb8e8e3d9aa0c2e72840329bfb5a740
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:

    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    rain()
<<<<<<< HEAD

=======
    
>>>>>>> 6eec79cd7bb8e8e3d9aa0c2e72840329bfb5a740
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
