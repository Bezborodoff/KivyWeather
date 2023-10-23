import sys
import os
#if sys.__stdout__ is None or sys.__stderr__ is None:
os.environ['KIVY_NO_CONSOLELOG'] = '1'
from kivy.resources import resource_add_path

from kivy.config import Config
Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '500')
Config.set('kivy','window_icon','icon-weather-app.ico')


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import  Screen
# время и дата
import datetime
from datetime import date
# import urllib library
from urllib.request import urlopen
import json

#импорт своего модуля конвертации дней недели
#1-Пн,2-Вт,3-Ср и т.д.
import dayWord as dw
#print(dw.DayA(3)) #среда

#этот кусок берет информацию с сайта
#url с текущей погодоой
url='https://api.openweathermap.org/data/2.5/weather?lat=55.7522&lon=37.6156&appid=39b390d2080e84bc8ece00b18120aaf8&units=metric&lang=RU'
#store the response of URL
response = urlopen(url)

#url с прогнозом на 16 дней
url_forecast='https://api.openweathermap.org/data/2.5/forecast/daily?lat=55.7522&lon=37.6156&appid=39b390d2080e84bc8ece00b18120aaf8&units=metric&lang=RU'
#store the response of URL
response_daily = urlopen(url_forecast)

#storing the JSON response 
#from url in data
data_json = json.loads(response.read())
data_json_daily = json.loads(response_daily.read())

# #print the json response
# #print(data_json)

# #Print json data using loop
# # for (key) in data_json:{
# #        print(key,":", data_json[key])
# # }
# print("name:", data_json['name'])
# print("temp:", data_json['main']['temp'])


#этот кусок читает из файла
# with open('weather.txt','r',encoding="utf-8") as f:
#     data = f.read()
#     data_json = json.loads(data)
# # print("name:", data_json['name'])
# # print("temp:", data_json['main']['temp'])
# #этот кусок читает из файла
# with open('daily.txt','r',encoding="utf-8") as fd:
#     data_daily = fd.read()
#     data_json_daily = json.loads(data_daily)

dicD_all = {}
dicDayW = {}
dicDay = {}
dicTemp_n = {}
dicTemp_d = {}
d=0
for i in data_json_daily['list']:
    dicDayW["day" + str(d)] = dw.DayA(datetime.datetime.utcfromtimestamp(i['dt']).weekday())
    dicDay["day" + str(d)] = datetime.datetime.utcfromtimestamp(i['dt']).strftime('%d.%m')
    dicTemp_n["dayTemp_n_" + str(d)] = i['temp']['night']
    dicTemp_d["dayTemp_d_" + str(d)] = i['temp']['day']
    dicD_all[d]=i
    d +=  1
    
#print(dic["day1"])
#print("data_json_daily: ", data_json_daily['list'][0]['temp']['day'])
#print(dicD_all[0]['weather'][0]['icon'])

name=data_json['name']
temp=data_json['main']['temp']
feels_like=data_json['main']['feels_like']
weather=data_json['weather']
weather_icon=data_json['weather'][0]['icon']
weather_desc=data_json['weather'][0]['description']
humidity=data_json['main']['humidity']
wind_speed=data_json['wind']['speed']

#print(weather[0]['icon'])

class Container(Screen): 
      
    def load_temp(self):
        # dat=1
        # for i in dic:
        #     print(dic["day" + str(dat)])
        #     self.link_day+ str(dat).text=dic["day" + str(dat)]    
        #     dat +=1
        
        #погодные иконки
        
        self.link_imgDay1.source=str("https://openweathermap.org/img/wn/"+str(dicD_all[0]['weather'][0]['icon'])+"@2x.png")
        self.link_imgDay2.source=str("https://openweathermap.org/img/wn/"+str(dicD_all[1]['weather'][0]['icon'])+"@2x.png")
        self.link_imgDay3.source=str("https://openweathermap.org/img/wn/"+str(dicD_all[2]['weather'][0]['icon'])+"@2x.png")
        self.link_imgDay4.source=str("https://openweathermap.org/img/wn/"+str(dicD_all[3]['weather'][0]['icon'])+"@2x.png")
        self.link_imgDay5.source=str("https://openweathermap.org/img/wn/"+str(dicD_all[4]['weather'][0]['icon'])+"@2x.png")
        self.link_imgDay6.source=str("https://openweathermap.org/img/wn/"+str(dicD_all[5]['weather'][0]['icon'])+"@2x.png")

        self.link_dayW1.text=dicDayW["day1"]
        self.link_day1.text=dicDay["day1"]
        self.link_dayTemp_n_1.text=str(dicTemp_n["dayTemp_n_1"])+"°"
        self.link_dayTemp_d_1.text=str(dicTemp_d["dayTemp_d_1"])+"°"

        self.link_dayW2.text=dicDayW["day2"]
        self.link_day2.text=dicDay["day2"]
        self.link_dayTemp_n_2.text=str(dicTemp_n["dayTemp_n_2"])+"°"
        self.link_dayTemp_d_2.text=str(dicTemp_d["dayTemp_d_2"])+"°"
        
        self.link_dayW3.text=dicDayW["day3"]
        self.link_day3.text=dicDay["day3"]
        self.link_dayTemp_n_3.text=str(dicTemp_n["dayTemp_n_3"])+"°"
        self.link_dayTemp_d_3.text=str(dicTemp_d["dayTemp_d_3"])+"°"

        self.link_dayW4.text=dicDayW["day4"]
        self.link_day4.text=dicDay["day4"]
        self.link_dayTemp_n_4.text=str(dicTemp_n["dayTemp_n_4"])+"°"
        self.link_dayTemp_d_4.text=str(dicTemp_d["dayTemp_d_4"])+"°"

        self.link_dayW5.text=dicDayW["day5"]
        self.link_day5.text=dicDay["day5"]
        self.link_dayTemp_n_5.text=str(dicTemp_n["dayTemp_n_5"])+"°"
        self.link_dayTemp_d_5.text=str(dicTemp_d["dayTemp_d_5"])+"°"
        
        self.link_dayW6.text=dicDayW["day6"]
        self.link_day6.text=dicDay["day6"]
        self.link_dayTemp_n_6.text=str(dicTemp_n["dayTemp_n_6"])+"°"
        self.link_dayTemp_d_6.text=str(dicTemp_d["dayTemp_d_6"])+"°"

        
        self.link_temp.text=str(temp)+"°"
        self.link_town.text=str(name)
        self.link_today.text=dw.DayA(date.today().weekday())
        
        self.link_img.source=str("https://openweathermap.org/img/wn/"+str(weather_icon)+"@2x.png")
        self.link_time.text=datetime.datetime.now().strftime("%H:%M")
        self.link_date.text=date.today().strftime("%d.%m.%Y")
        self.link_weather_desc.text=str(weather_desc)
        self.link_main_hum.text="влажность: "+str(humidity)+"%"
        self.link_main_wind_speed.text="ветер: "+str(wind_speed)+" м/с"
        self.link_feels_like.text="feels like: "+str(feels_like)+"°"
       
buildKV = Builder.load_file("Weather.kv")

class WeatherApp(App):
    def build(self):
        self.icon = "icon-weather-app.png"
        return buildKV

if __name__=="__main__":
    # these lines should be added
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    ###
    WeatherApp().run()
    