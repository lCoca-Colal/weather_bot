import requests
import datetime
from pprint import pprint 
from conifg import open_weather_token

def get_weather(city, open_weather_token):
    
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    
    }
    
    try:
        r = requests.get(
            f"Https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        #print(data)
        
        city = data["name"]
        cur_weather = data["main"]["temp"]
        
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"
        
        humidity = data["main"]["humidity"]
        max_temp = data["main"]["temp_max"] 
        min_temp = data["main"]["temp_min"]
        feel = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        sunrise_time = datetime.datetime.fromtimestamp(data['sys']["sunrise"])
        sunset_time = datetime.datetime.fromtimestamp(data['sys']["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']["sunset"]) - datetime.datetime.fromtimestamp(data['sys']["sunrise"])
        
        print (f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
               f"Погода в городе: {city}\nТемпература: {cur_weather} C° {wd}\nМакс. температура: {max_temp} C°\nМин. температура: {min_temp} C°\n"
               f"Ощущение: {feel}C°\nДавление: {pressure} мм.рт.ст.\nВлажность: {humidity}%\nВетер: {wind}м/с\n"
               f"Восход солнца: {sunrise_time}\nЗакат солнца: {sunset_time}\nПродолжительность дня: {length_of_the_day}\n"
               f"Хорошего Дня!")
    except Exception as ex:
        print("ex")
        print("Проверьте название города")

def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)
    
    
    
if __name__ == "__main__":
    main() 