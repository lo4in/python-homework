import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # For temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    


    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Failed to fetch weather data. HTTP Status Code: {response.status_code}")

def display_weather(data):
    city = data.get("name")
    temperature = data["main"].get("temp")
    humidity = data["main"].get("humidity")
    weather_desc = data["weather"][0].get("description")
    
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_desc.capitalize()}")

# Main execution
API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
CITY_NAME = "Tashkent"

try:
    weather_data = get_weather(CITY_NAME, API_KEY)
    display_weather(weather_data)
except Exception as e:
    print(e)
