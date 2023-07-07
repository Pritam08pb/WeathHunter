import schedule
import time
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime, timedelta

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
          
    return temperature,wind,hum,otime

# def data(temperature, wind,hum, otime):
#     data = [[temperature, wind,hum, otime, datetime.now().strftime("%Y-%m-%d")]]
#     with open("weather_dataset.csv", "r") as file:
#         reader = csv.reader(file)
#         last_row = list(reader)[-1]
#         time = str(last_row[3])
#         if otime != time:
#              with open("weather_dataset.csv", "a", newline="") as file:
#                writer = csv.writer(file)
#                writer.writerows(data)
         

# def schedule_scraping():
#     schedule.every(1).minutes.do(scrape)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)


# def main():
#     temperature, wind, hum, otime = scrape()
#     data(temperature, wind,hum, otime)

# if __name__ == "__main__":
#     main()
#     schedule_scraping()
