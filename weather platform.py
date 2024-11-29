import requests

key = "f81703c1f3b81ad93e6644153c4a426e"
cityname = "Житомир"
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={key}")

a = response.json()
print(a)
print(a["main"])
print(a["main"]['temp']-273.15)

