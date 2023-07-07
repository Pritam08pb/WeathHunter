from flask import Flask, jsonify
import scrapy as sc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST", "GET"])
def predict_weather():
    # Scrape weather data
    temperature, wind, hum, otime = sc.scrape()
    sc.data(temperature, wind, hum, otime)

    predicted_weather = "down"
  
    # Create a response dictionary
    response = {
        "temperature": temperature,
        "wind": wind,
        "humidity": hum,
        "predicted_weather": predicted_weather
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
