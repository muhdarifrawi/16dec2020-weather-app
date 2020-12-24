from flask import Flask, render_template
import requests
from datetime import datetime, time

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    warm_light = ["Cloudy","Hazy","Slightly Hazy","Mist","Light Rain","Moderate Rain","Heavy Rain",
                    "Heavy Showers","Thundery Showers","Heavy Thundery Showers","Heavy Thundery Showers with Gusty Winds"]
    cool_light = ["Fair","Fair & Warm","Partly Cloudy","Windy","Passing Showers","Showers"]

    time_now = datetime.now().isoformat(timespec="seconds")
    print("datetime: ",time_now.replace(":","%3A"))
    full_datetime = time_now.replace(":","%3A")

    # Use the date_time parameter to retrieve the latest forecast issued at that moment in time.
    data_now = requests.get("https://api.data.gov.sg/v1/environment/24-hour-weather-forecast?date_time={full}".format(full=full_datetime))
    
    current_forecast = data_now.json()["items"][0]["general"]["forecast"]
    for i in warm_light:
        if i == current_forecast:
            print("warm")
    
    for i in cool_light:
        if i == current_forecast:
            print("cool")

    # Use the date parameter to retrieve all of the forecasts issued for that day
    data_forecast = requests.get("https://api.data.gov.sg/v1/environment/24-hour-weather-forecast")
    return render_template("index.html", dataNow=data_now.json())


# this is only for development and not recommended to leave it this way
if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=8080,
            debug=True)