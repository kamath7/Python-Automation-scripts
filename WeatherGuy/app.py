from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()

WEATHER_API_KEY=os.getenv('WEATHER_API_KEY')

r = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q=Mangalore&appid={WEATHER_API_KEY}")



def get_clean_time(time1):
    return  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time1)))


def get_weather_for_city(cityName):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={cityName}&appid={WEATHER_API_KEY}")
    content = r.json()
    weather_data = content['list']

    header = "City, DateTime, Temperature, Description"
    with open(f'{cityName}.txt','a') as f:
        f.write(header + "\n")
        f.close
    for weather in weather_data:
        with open(f'{cityName}.txt','a') as f:
            my_string = f"{cityName}, {get_clean_time(weather['dt'])}, {weather['main']['temp']}, {weather['weather'][0]['description']}\n"
            f.write(my_string)
        


get_weather_for_city('Mangalore')
    # for weather in weather_data:
    #     print('Mangalore',get_clean_time(weather['dt']), weather['main']['temp'], weather['weather'][0]['description'])
    #     print('Adding to file')

# print(weather_data[0]['main']['temp'],' ',weather_data[0]['weather'][0]['description'],time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(weather_data[0]['dt']))))