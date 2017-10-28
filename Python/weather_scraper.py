import requests
import time

from bs4 import BeautifulSoup

def get_by_class(tags, class_name):
    for tag in tags.find_all():
        if class_name in tag.get('class', ''):
            return tag

def get_forecast_for_day(day):
    forecast = dict()

    weather_data = get_by_class(day, 'short')
    forecast['condition'] = get_by_class(weather_data, 'wx-text').text
    forecast['high'] = get_by_class(weather_data, 'wx-high').text
    forecast['low'] = get_by_class(weather_data, 'wx-low').text
    forecast['precip'] = get_by_class(weather_data, 'wx-precip').text

    datetime =  get_by_class(day, 'dateTime').get('data-time')
    datetime = time.gmtime(int(datetime[0:-3]))
    forecast['datetime'] = time.strftime('%x', datetime)

    return forecast

def get_daily_forecasts():
    response = requests.get('http://katu.com/weather')
    response.raise_for_status()
    html = BeautifulSoup(response.text, 'html.parser')

    return [div for div in html.find_all('div') if 'daily-forecast' in div.get('class', '')]

if __name__ == '__main__':
    print(f'''

_____           _   _                 _  __          __        _   _
|  __ \         | | | |               | | \ \        / /       | | | |
| |__) |__  _ __| |_| | __ _ _ __   __| |  \ \  /\  / /__  __ _| |_| |__   ___ _ __
|  ___/ _ \| '__| __| |/ _` | '_ \ / _` |   \ \/  \/ / _ \/ _` | __| '_ \ / _ \ '__|
| |  | (_) | |  | |_| | (_| | | | | (_| |    \  /\  /  __/ (_| | |_| | | |  __/ |
|_|   \___/|_|   \__|_|\__,_|_| |_|\__,_|     \/  \/ \___|\__,_|\__|_| |_|\___|_|



''')
    daily_forecasts = get_daily_forecasts()

    for day in daily_forecasts:
        forecast = get_forecast_for_day(day)

        print(f'''{'-' * 30}
Forecast for {forecast["datetime"]}:
    High: {forecast["high"]}
    Low: {forecast["low"]}
    Chance of Precipitation: {forecast["precip"]}''')
