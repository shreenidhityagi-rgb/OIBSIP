# Basic Weather App
# Oasis Infobyte Python Programming Internship - Task 3

import requests

print("Basic Weather App")

city = input("Enter city name: ")

# IMPORTANT: Replace YOUR_API_KEY with your actual API key
api_key = "7a0dfa6ba9d78e662ffc939715aa29c3"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    weather_condition = data["weather"][0]["description"]

    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Weather Condition:", weather_condition)
else:
    print("Error: City not found or API issue")
