from prefect import flow, task
import requests
import pandas as pd
from datetime import datetime

@task
def fetch_weather(city: str, api_key: str):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

@task
def save_to_csv(data: dict, city: str):
    filename = f"{city}_weather_log.csv"
    df = pd.DataFrame([{
        "city": city,
        "temperature": data['current']['temp_f'],
        "condition": data['current']['condition']['text'],
        "timestamp": datetime.now()
    }])
    df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)

@flow
def daily_weather_pipeline():
    city = "Atlanta"
    api_key = "your_weather_api_key"
    data = fetch_weather(city, api_key)
    save_to_csv(data, city)

if __name__ == "__main__":
    daily_weather_pipeline()
