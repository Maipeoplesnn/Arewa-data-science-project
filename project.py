import requests

API_KEY = 'e3f74116d21f0d98099a1c3151a6a44f'
city = 'Lagos'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

response = requests.get(url)
data = response.json()

print(data)  # Print the data to see the structure
data = response.json()

print(data)  # Print the data to see the structure
