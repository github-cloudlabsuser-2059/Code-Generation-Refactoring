import requests

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(data):
    if data and data.get("main"):
        city = data["name"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Description: {desc}")
        print(f"Humidity: {humidity}%")
    else:
        print("Could not retrieve weather information.")

def main():
    print("OpenWeatherMap Console App")
    city = input("Enter city name: ")
    data = get_weather(city)
    display_weather(data)

if __name__ == "__main__":
    main()