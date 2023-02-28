#Created by Michael Speer
#This integrated with my ListenerBot will help develop a predictive model for how busy of a day my group chat will be.

import urllib.request
import time
import json

#The use of a simple config allows to keep sensitive info like keys and zip codes secret.
f = open('config.json')
config = json.load(f)
ziparray = config['zip']

while(True):
    with open('weather_data.json', 'a') as jsonfile:
        jsonfile.write('"time":'+str(time.time()))
    for zip_code in ziparray:
        url = 'https://api.openweathermap.org/data/2.5/weather?zip='+zip_code+',US&appid='+config['keys']['OpenWeatherKey']
        e = urllib.request.urlopen(url)
        response = e.read().decode('utf-8')
        print(response)
        with open('weather_data.json', 'a') as jsonfile:
            jsonfile.writelines(response)
    time.sleep(300)