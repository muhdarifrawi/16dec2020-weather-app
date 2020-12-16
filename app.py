from flask import Flask, render_template
import requests
from datetime import datetime, time

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = requests.get("https://api.data.gov.sg/v1/environment/24-hour-weather-forecast")
    # print(data)
    now = datetime.now().isoformat(timespec="seconds")
    strp_now = datetime.strptime(str(now),"%Y-%m-%dT%H:%M:%S")
    print("datetime: ",strp_now)
    return render_template("index.html")