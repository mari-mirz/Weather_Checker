import logging
import weather_checker

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    will_rain = weather_checker.rain
    
    return func.HttpResponse(
            will_rain,
            status_code=200
    )
