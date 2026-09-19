import logging
import azure.functions as func
import json
import requests
from datetime import datetime

app = func.FunctionApp()

@app.timer_trigger(schedule="15 */15 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False)
@app.blob_output(arg_name="outputblob",
                 path="weather-data/temperature_{datetime.now()}.json",
                 connection="MyBlobConnection") 
def weathertest(myTimer: func.TimerRequest, outputblob: func.Out[str]) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    api_url = "https://api.open-meteo.com/v1/forecast?latitude=28.6519&longitude=77.2315&models=best_match&current=temperature_2m&timezone=auto"

    try:

        response = requests.get(api_url)
        response.raise_for_status()

        json_string = json.dumps(response.json())
        outputblob.set(json_string)

        logging.info('Successfully fetched API data and saved JSON to Blob Storage.')

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch data from URL: {e}")