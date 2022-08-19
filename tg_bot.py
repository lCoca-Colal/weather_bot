import requests
import datetime
from conifg import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['\start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне город и я пришлю сводку погоды)")
    
    
@dp.message_handler()
async def get_weather(message: types.Message):
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
            f"Https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
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
        
        await message.reply (f"***\{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}/***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather} C° {wd}\nМакс. температура: {max_temp} C°\nМин. температура: {min_temp} C°\n"
            f"Ощущение: {feel}C°\nДавление: {pressure} мм.рт.ст.\nВлажность: {humidity}%\nВетер: {wind}м/с\n"
            f"Восход солнца: {sunrise_time}\nЗакат солнца: {sunset_time}\nПродолжительность дня: {length_of_the_day}\n"
            f"Хорошего Дня!")
    
    except:
        await message.reply("Проверьте название города")
    
    
      
if __name__ == '__main__':
    executor.start_polling(dp)
    