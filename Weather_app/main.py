from typing import Any, Dict, List
import requests
import sys

class WeaterExption(ValueError):
    def __init__(self, msg: str):
        super().__init__(msg);

def get_weather(city) -> Dict[str, float]:
    Api_Key = "a832ee34727b110f62ba1e479b9bb37c"
    if not city:
        raise WatherExption("City Not Found");
    #request to get the cooredonite the city(lat, lon)
    response = requests.get(
        "https://api.openweathermap.org/geo/1.0/direct",
        params={
            "q": city,
            "limit": 1,
            "appid": Api_Key
        }
        )
    if response.ok: 
        data: List[Dect[str, Any]] = response.json();
    else : raise WeaterExption(f"Error : {response.status_code}:reason: {response.reason}")

    #request to get the description and the temp. 
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "lat": data[0]["lat"],
            "lon": data[0]["lon"],
            "units": "metric",
            "appid": Api_Key
        }
    )   
    if response.ok:
        data2 = response.json();
    else : raise WeaterExption(f"Error : {response.status_code}:reason: {response.reason}")
    return {
            "name" : data[0]["name"],
            "lat" : data[0]['lat'],
            "lon" : data[0]['lon'],
            "description" : data2['weather'][0]['description'],
            "country": data2['sys']['country'],
            "time_zone" : data2['timezone']
            };
def display_data(data):
    print(f"Time Zone: {data['name']}")
    print(f"Lat: {data['lat']}")
    print(f"Lon: {data['lon']}")
    print(f"description : {data['description']}")
    print(f"country: {data['country']}")
    print(f"Time Zone: {data['time_zone']}")

def main():
    print("===Weather App===")
    print();
    city = input("Plase Enter The City name :");
    try:
        data = get_weather(city);
        display_data(data);
    except ValueError as e:
        print(e);
        sys.exit(1);
if __name__ == "__main__":
    main()
