from flask import Flask, jsonify, request
import model
import scrapy as sc

app = Flask(__name__)


@app.route("/predict_weather", methods=["POST"])
def predict_weather():
    # Get input parameters from the request
    data = request.get_json()
    date = data["date"]
    location = data["location"]

    temperature, wind, hum, otime = sc.scrape()
    sc.store_weather_data(temperature, wind, hum, otime)
    dataset = sc.load_weather_dataset()

    # Make predictions using the loaded model
    # Replace this with your actual prediction logic
    predicted_weather = model.predict([[date, location]])

    # Create a response dictionary
    response = {
        "date": date,
        "location": location,
        "predicted_weather": predicted_weather
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run()
