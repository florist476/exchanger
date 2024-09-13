import requests

valcode = input('Введіть валюту ')
date = input("Введіть дату без крупок за принципом yyyymmdd ")
response = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={date}&json")
a = response.json()
cash = int(input("Кількість банкнот?"))

print(a[0]["txt"])

print(a[0]["cc"])

print(a[0]["rate"] * cash)

