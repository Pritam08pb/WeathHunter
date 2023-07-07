from flask import Flask, jsonify
import scrapy as sc
from flask_cors import CORS
import schedule
import time
import requests
from bs4 import BeautifulSoup
import csv
import datetime

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST", "GET"])
def predict_weather():
    # Scrape weather data

    url = "https://mausam.imd.gov.in/bhubaneswar/" 
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    temperature = soup.find("div", class_="temp").text
    wind = soup.find("li", class_="sun-info").text
    otime = soup.find("small", class_="small").text
    hum = soup.find("div", id="temperature1").text
    current_datetime = datetime.datetime.now()

    temperature = temperature[1:3]
    wind = wind
    otime = str(otime[18:])
    hum = hum[1:]
    current_date = current_datetime.date()
    
    
    # Create a response dictionary
    response = {
        "temperature": temperature,
        "wind": wind,
        "humidity": hum,
        "observation_time": otime,
        "current date": current_date
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
