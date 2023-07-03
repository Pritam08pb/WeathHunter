import schedule
import time
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Scraping weather
def scrape():
    url = "https://mausam.imd.gov.in/bhubaneswar/" 
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    temperature = soup.find("div", class_="temp").text
    wind = soup.find("li", class_="sun-info").text
    otime = soup.find("small", class_="small").text
    hum = soup.find("div", id="temperature1").text

    temperature = temperature[1:3]
    wind = wind
    otime = str(otime[18:])
    hum = hum[1:]
    data = [[temperature, wind,hum, otime, datetime.now().strftime("%Y-%m-%d")]]
    with open("weather_dataset.csv", "r") as file:
        reader = csv.reader(file)
        last_row = list(reader)[-1]
        time = str(last_row[3])
        if otime != time:
             with open("weather_dataset.csv", "a", newline="") as file:
               writer = csv.writer(file)
               writer.writerows(data)
    return temperature,wind,hum,otime



# def schedule_scraping():
#     schedule.every(1).minutes.do(scrape)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)


def main():
    temperature, wind, hum, otime = scrape()

if __name__ == "__main__":
    main()
    #schedule_scraping()
