# 🌤️ Weather Data Pipeline with Prefect

This project demonstrates how to use Prefect to orchestrate a simple data pipeline that fetches current weather data from a public API and logs it to a CSV file for tracking and analysis.

---

## 🚀 Features

- Fetches live weather data from [WeatherAPI](https://www.weatherapi.com/)
- Logs temperature, condition, and timestamp to a local CSV file
- Uses `Prefect` to orchestrate the workflow
- Easily extendable to multiple cities or data destinations
- Deployable to [Prefect Cloud](https://app.prefect.cloud/)

---

## 🧠 Skills Demonstrated

Orchestration with `Prefect`

Working with external APIs `(requests)`

Data transformation and export using `pandas`

Automation and scheduling with Python

Lightweight logging with timestamping

Cloud deployment using Prefect Cloud

---

## 📂 Project Structure
```
weather-pipeline/
├── weather_pipeline.py # Main flow definition
├── README.md # Project documentation
└── requirements.txt # Dependencies
```
---
## ⚙️ How It Works
`fetch_weather`: Pulls current weather data from WeatherAPI.

`save_to_csv`: Logs the temperature, condition, and timestamp to a CSV file.

`daily_weather_pipeline`: Prefect `@flow` that links it all together and is deployable locally or to Prefect Cloud.


## 🚀 Quick Start

1. Download or copy the `weather_pipeline.py` file.
2. Add your WeatherAPI key in the script.
3. Install required libraries:
   ```bash
   pip install prefect pandas requests
   ```
## 4. Run:

```
python weather_pipeline.py
````

## ☁️ Cloud Deployment
This flow is also compatible with Prefect Cloud. You can log into your Prefect Cloud workspace, register the flow, and schedule it to run automatically.

## 📝 Example Output
```
city,temperature,condition,timestamp
Atlanta,78.4,Partly cloudy,2025-07-21 07:45:02
```
## 💡 Why This Project?
I created this project to explore workflow orchestration tools and practice automated data logging—skills relevant for data engineering, analytics automation, and AI pipeline building. It’s part of my broader portfolio exploring how to use data and automation to improve decision-making.


