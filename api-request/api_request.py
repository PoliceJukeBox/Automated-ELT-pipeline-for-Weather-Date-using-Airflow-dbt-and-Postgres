import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

api_url = f"{BASE_URL}?access_key={API_KEY}&query=New York"

def fetch_data():
    response = requests.get(api_url)
    print(response)

fetch_data()