import datetime
import requests
import json
from prettytable import PrettyTable 
from pprint import pprint

#Create table object.
tbl = PrettyTable()

while True:
    option = ["yes","no"]
    #print(option)
    choise = input("Press y for continue/press n for stop: ")
    if choise == 'y':
        city_name = input("Enter City Name: ")

        #Our api key.
        api_key = 'b402c46c9e7b6c12f101a1fb89db7779'
        complete_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b402c46c9e7b6c12f101a1fb89db7779&units=metric'.format(city_name)
        response = requests.get(complete_url)

        #Json data Object.
        data = response.json()
        #pprint(data)
        print()
        #Extract data.
        date_time = datetime.datetime.fromtimestamp(data['dt'])
        name = data['name']
        temp = data['main']['temp']
        temp_feels = data['main']['feels_like']
        humdty = data['main']['humidity']
        wind = round(data['wind']['speed'] * 1.609,2)  #Convert miles/h into Km/h.
        desc = data['weather'][0]['description']
        tbl.add_row([date_time,name,temp,temp_feels,humdty,wind,desc])

        #Display data in normal way.
        print("Date/Time",date_time)
        print("City Name: ",name)
        print("Tempreture is: ",temp,"Celious")
        print("Tempreture feels like: ",temp_feels,"Celious")
        print("Humidity: ",humdty,"%")
        print("Wind Speed is ",wind,"km/h")
        print("Description is: ",desc)
        print()
    if choise == 'n':
        break
print()
    
#Create table for represent data.
tbl.field_names = ["Date/Time","State/City Name","Tempreture(°C)","Tempreture Feels(°C)","Humidity(%)","Wind Speed(Km/h)","Description"]
print(tbl)

weather_txt = tbl.get_string(title = "CURRENT WEATHER DATA")
with open('weather output.txt','w') as fw:
    fw.write(weather_txt)
    print("Weather Data File Store Sucessfully. ")
    fw.close()

print()

with open('Weather output.txt', 'r') as fr:
    print(fr.read())
    print("File read sucessfully. ")
