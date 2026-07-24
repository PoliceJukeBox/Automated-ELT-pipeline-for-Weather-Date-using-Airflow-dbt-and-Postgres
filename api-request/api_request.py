import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

api_url = f"{BASE_URL}?access_key={API_KEY}&query=New York"

def fetch_data():
    print(f"Fetching weather data from API: {api_url}")
    try:

        response = requests.get(api_url)
        response.raise_for_status()  
        print("Data fetched successfully from API")
        # print(f"Response JSON: {response.json()}")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        raise

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-07-24 10:08','localtime_epoch': 1784887680, 'utc_offset': '-4.0'}, 'current': {'observation_time': '02:08 PM', 'temperature': 22, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '05:46 AM', 'sunset': '08:19 PM', 'moonrise': '05:00 PM', 'moonset': '01:05 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 74}, 'air_quality': {'co': '238', 'no2': '27.7', 'o3': '68', 'so2': '3.1', 'pm2_5': '19.7', 'pm10': '22.6', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 7, 'wind_degree': 79, 'wind_dir': 'E', 'pressure': 1025, 'precip': 0, 'humidity': 49, 'cloudcover': 0, 'feelslike': 24, 'uv_index': 3, 'visibility': 16, 'is_day': 'yes'}}