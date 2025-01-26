import requests

API_KEY = '3aaa575bac929632e1e00cf301565205'
city = 'Kano'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
response = requests.get(url)
data = response.json()

print(data)  # Print the data
