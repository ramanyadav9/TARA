import requests
# from Tara.config import WEATHER_API_KEY
# from config import 
# 
WEATHER_API_KEY = "65bcd1a9e6426bfacc863a4a92ccabcf"


def get_weather(city):
    """
    Fetches weather details for a given city.
    :param city: City name as a string.
    :return: Weather details as a string.
    """
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            weather_info = (
                f"The weather in {city} is currently {weather_desc} with a temperature of {temperature}°C, "
                f"humidity of {humidity}%, and wind speed of {wind_speed} m/s."
            )
            return weather_info
        else:
            return "Sorry, I couldn't fetch the weather. Please check the city name."

    except Exception as e:
        return f"Error fetching weather: {e}"
