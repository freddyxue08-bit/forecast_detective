import httpx
response = httpx.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={
        "name": "Toronto",
        "count": 1,
        "language": "en",
    },
)
response.raise_for_status()
data=response.json()
city = data["results"][0]
print(f"{city["name"]}, {city["country"]}: {city["latitude"]}, {city["longitude"]}")
response = httpx.get(
    "https://archive-api.open-meteo.com/v1/archive",
    params={
        "latitude": city['latitude'],
        "longitude": city['longitude'],
        "start_date": "2025-01-01",
        "end_date": "2025-12-31",                               # last day of 2025, same format as start_date
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,daylight_duration",  # min temp, rainfall, daylight; no spaces
        "timezone": "auto",
    },
)
response.raise_for_status()
weather=response.json()
print(weather["daily"].keys())
print(len(weather["daily"]["time"]))