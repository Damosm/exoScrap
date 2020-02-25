import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

#Ex1###########################################
# x = requests.get('https://fr.wikipedia.org/robots.txt')

#print(x.text)

#Ex2##########################################
# x = requests.get('https://www.data.gov/')

# soup = BeautifulSoup(x.content)

# for p in soup.find('a', attrs={"href":u"/metrics"}):
    
    # print (p)

#ex3###############################################

# x = requests.get('https://www.linkedin.com/')

# soup = BeautifulSoup(x.content)

# ls=[]

# for p in soup.find('h1'):
    
#     ls.append(p)

# print(ls)

#ex4#########################################################


# x = requests.get('https://en.wikipedia.org/wiki/Main_Page')

# soup = BeautifulSoup(x.content,"lxml")

# ls=[]



# for p in soup.find('head'):
    
#     ls.append(p)

# for i in ls :
#     print(i)
# print(ls)

#ex5####################################################

# x = requests.get('https://fr.wikipedia.org/wiki/%C3%89lisabeth_II')

# soup = BeautifulSoup(x.content,"html.parser")

# s= soup.find(id='mw-content-text')

# tab_img = s.find_all('img')
# print(len(tab_img))

#ex6######################################################

# x = requests.get('https://twitter.com/EmmanuelMacron?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor')

# soup = BeautifulSoup(x.content,"html.parser")

# s = soup.find_all('a', attrs={'href':'/EmmanuelMacron/followers'})

# for i in s :
#     print(i.get('title'))
    
#ex7##############################################################


# x = requests.get('https://openweathermap.org/city/6454307')

# soup = BeautifulSoup(x.content,"html.parser")
# id1 = soup.find('div',id='widget') 
# id2 = id1.find('div')
# print(id1.get('div'))

# x = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=6454307&APPID=f38aa4800b84be81802294854cb750b6')

# x = requests.get('http://api.openweathermap.org/data/2.5/forecast?APPID=f38aa4800b84be81802294854cb750b6&q=nancy')

#with soup

# # soup = BeautifulSoup(x.content,"html.parser")
# # print(soup)

#with json

# data=x.json()
# json.dumps(data,indent=2)
# pprint(data)
######################################################################""

# Enter your API key here 
api_key = "f38aa4800b84be81802294854cb750b6"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
city_name = input("Enter city name : ") 

# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

# get method of requests module 
# return response object 
response = requests.get(complete_url) 
print(response)
# json method of response object
# convert json format data into 
# python format data 
x = response.json() 

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 

    # store the value of "main" 
    # key in variable y 
    y = x["main"]

    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"]

    # store the value corresponding 
    # to the "pressure" key of y 
    current_pressure = y["pressure"] 

    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 

    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z 
    weather_description = z[0]["description"] 

    # print following values 
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 

else: 
    print(" City Not Found ")