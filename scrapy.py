import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
otime=""
# Scraping weather
def scrape():
    url = "https://mausam.imd.gov.in/bhubaneswar/" 
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    temperature = soup.find("div", class_="temp").text
    wind = soup.find("li", class_="sun-info").text
    otime = soup.find("small", class_="small").text
    temperature = temperature[1:3]
    wind = wind
    otime = str(otime[18:])
    return temperature,wind,otime

def store_weather_data(temperature, wind, otime):
    data = [[temperature, wind, otime, datetime.now().strftime("%Y-%m-%d")]]
    with open("weather_dataset.csv", "r") as file:
        reader = csv.reader(file)
        last_row = list(reader)[-1]
        time = str(last_row[2])
        if otime != time:
             with open("weather_dataset.csv", "a", newline="") as file:
               writer = csv.writer(file)
               writer.writerows(data)

# Load weather dataset from CSV
def load_weather_dataset():
    dataset = []
    with open("weather_dataset.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            dataset.append(row)
    return dataset




def main():
    temperature,wind,otime= scrape()
    store_weather_data(temperature, wind, otime)
    dataset = load_weather_dataset()
    # predict_weather(dataset)
    
if __name__ == "__main__":
    main()



