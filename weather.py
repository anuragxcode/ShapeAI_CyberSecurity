import requests
#import os
from datetime import datetime
    
api_key = 'aa55f2220ec6f58207572417df7b2335'
location = input("Enter the city name: ")

text_file = open("weather.txt", "w")

#Opens or creates the .txt file, sharing the directory of the script#
text_file.write(location)
#Writes the variable into the .txt file#


complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data

temp_city = ((api_data['main']['temp']) - 273.15)
strtemp_city = str(temp_city)
text_file.write(strtemp_city)

weather_desc = api_data['weather'][0]['description']
strweather_desc = str(weather_desc)
text_file.write(strweather_desc)

hmdt = api_data['main']['humidity']
strhmdt = str(hmdt)
text_file.write(strhmdt)

wind_spd = api_data['wind']['speed']
strwind_spd = str(wind_spd)
text_file.write(strwind_spd)

date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
strdate_time = str(date_time)
text_file.write(strdate_time)

text_file.close()
#Closes the .txt file#

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')



