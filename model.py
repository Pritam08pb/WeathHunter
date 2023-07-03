import pandas as pd
from sklearn.linear_model import LinearRegression
import scrapy as sc

def preprocess_wind(wind):
    # Extract numerical value from wind string
    wind_speed = float(wind.split()[1])
    return wind_speed

def preprocess_humidity(humidity):
    # Remove percentage sign and convert to float
    humidity_value = float(humidity.rstrip('%'))
    return humidity_value

def preprocess_time(update_time):
    # Convert string to timestamp
    timestamp = pd.to_datetime(update_time).timestamp()
    return timestamp

def pred():
    # Load the CSV data
    data = pd.read_csv("weather_dataset.csv")

    # Preprocess the data
   
    data['wind_speed'] = data['wind'].apply(preprocess_wind)
    data['humidity'] = data['humidity'].apply(preprocess_humidity)

    # Split the data into features (X) and target variable (y)
    X = data[[ 'wind_speed', 'humidity']]
    y = data['temperature']

    # Create and train the Linear Regression model
    model = LinearRegression()
    model.fit(X, y)

    # Preprocess the input data
    temperature, wind, hum, otime = sc.scrape()
    
    new_wind = preprocess_wind(wind)
    new_humidity = preprocess_humidity(hum)

    # Predict weather for new observation
    
    new_data = pd.DataFrame({'wind_speed': [new_wind], 'humidity': [new_humidity]})
    predicted_temperature = model.predict(new_data)

    return predicted_temperature

