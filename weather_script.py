import requests
import os

def fetch_weather(city: str, api_key: str) -> dict | None:
    """Fetch weather data for a given city from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Network error: {err}")
    return None

def display_weather(data: dict, city: str) -> None:
    """Display weather information from the API response."""
    if not data or 'main' not in data or 'weather' not in data:
        print("Error: Invalid weather data received.")
        return
    main = data['main']
    weather = data['weather'][0]
    print(f"Weather in {city}: {weather['description'].title()}")
    print(f"Temperature: {main['temp']}°C")
    print(f"Humidity: {main['humidity']}%")

def main():
    city = input("Enter city name: ").strip()
    api_key = os.getenv("OPENWEATHER_API_KEY") or input("Enter your OpenWeatherMap API key: ").strip()
    if not city:
        print("City name cannot be empty.")
        return
    if not api_key:
        print("API key cannot be empty.")
        return
    data = fetch_weather(city, api_key)
    if data and data.get("cod") == 200:
        display_weather(data, city)
    else:
        print(f"Error fetching weather data: {data.get('message', 'Unknown error') if data else 'No data returned.'}")

if __name__ == "__main__":
    main()