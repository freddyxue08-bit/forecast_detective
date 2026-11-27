import httpx
response=httpx.get("https://geocoding-api.open-meteo.com/v1/search",params={"name":"Toronto","count":1,"language":"en"},)
response.raise_for_status()
data=response.json()
city = data["results"][0]
print(f"{city["name"]}, {city["country"]}: {city["latitude"]}, {city["longitude"]}")
