import requests

API_KEY = "1712870671c73becd6266fc8bb036f0a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city_name = input("Enter city name: ")
request_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature = main['temp']
    humidity = main['humidity']
    pressure = main['pressure']
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
