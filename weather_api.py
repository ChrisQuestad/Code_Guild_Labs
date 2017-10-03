# temp, wind direction, conditions
import requests


city = input('Please enter your City name: ')
package = {
    'APPID': "536740eef37be6ad7b9a6a3d0f5f5cd1",
    'q': city
}
r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)
data = r.json()


def temps():
    temperature = input('Would you like your temp displayed as C, or F?: ')
    if temperature.lower() == 'c':
        c_temp = int(data['main']['temp'] - 273)
        print(c_temp)
    elif temperature.lower() == 'f':
        f_temp = int(data['main']['temp'] * (9/5) - 459.67)
        print(f_temp)
    else:
        print(data['main']['temp'])

temps()
print(int(data['wind']['deg']))
print(data['weather'][0]['description'])
