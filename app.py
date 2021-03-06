from flask import Flask, render_template
import requests
from datetime import datetime, time

# for rpi GPIO functionality
# import RPi.GPIO as GPIO
# import pigpio

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarning(False)

blue = 20
red = 16
green = 12

# pi = pigpio.pi()

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    warm_light = ["Cloudy","Hazy","Slightly Hazy","Mist","Light Rain","Moderate Rain","Heavy Rain",
                    "Heavy Showers","Thundery Showers","Heavy Thundery Showers","Heavy Thundery Showers with Gusty Winds"]
    cool_light = ["Fair","Fair & Warm","Partly Cloudy","Windy","Passing Showers","Showers"]


    # generate greeting
    greeting = ""

    hour_time_24h = int(datetime.now().strftime("%H"))

    if hour_time_24h >= 22 and hour_time_24h<5:
        greeting = "Good Night"
    elif hour_time_24h >= 5 and hour_time_24h<12:
        greeting = "Good Morning"
    elif hour_time_24h >= 12 and hour_time_24h<17:
        greeting = "Good Afternoon"
    elif hour_time_24h >= 17 and hour_time_24h<22:
        greeting = "Good Evening"
    else:
        print("unexpected error")

    #  check for ISO time
    time_now = datetime.now().isoformat(timespec="seconds")
    print("datetime: ",time_now.replace(":","%3A"))
    full_datetime = time_now.replace(":","%3A")

    # Use the date_time parameter to retrieve the latest forecast issued at that moment in time.
    data_now = requests.get("https://api.data.gov.sg/v1/environment/24-hour-weather-forecast?date_time={full}".format(full=full_datetime))

    # current forecast using 2hourly data
    forecast_now = requests.get("https://api.data.gov.sg/v1/environment/2-hour-weather-forecast?date_time={full}".format(full=full_datetime))

    
    current_area = forecast_now.json()["area_metadata"][38]["name"]
    current_forecast = forecast_now.json()["items"][0]["forecasts"][38]["forecast"]
    print(current_forecast)
    for i in warm_light:
        if i == current_forecast:
            print("warm")
            # rgb 235, 180, 52
            # pi.set_PWM_dutycycle(red,0)
            # pi.set_PWM_dutycycle(green,240)
            # pi.set_PWM_dutycycle(blue,255)
           
    
    for i in cool_light:
        if i == current_forecast:
            print("cool")
            # pi.set_PWM_dutycycle(red,0)
            # pi.set_PWM_dutycycle(green,0)
            # pi.set_PWM_dutycycle(blue,0)
            

    # Use the date parameter to retrieve all of the forecasts issued for that day
    data_forecast = requests.get("https://api.data.gov.sg/v1/environment/24-hour-weather-forecast")
    return render_template("index.html", dataNow=data_now.json(), currentForecast=current_forecast, currentArea=current_area, greeting=greeting)


# this is only for development and not recommended to leave it this way
if __name__ == "__main__":
    app.run(host="127.0.0.1",
            port=8080,
            debug=True)