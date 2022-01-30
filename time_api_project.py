import requests
import re
URL = "http://worldtimeapi.org/api/timezone/"
continent = input("Enter the continent: ").strip()
list = input("Enter the city: ").strip()
city = re.sub(r" ", "_",list)
request_url = f"{URL}{continent}/{city}"
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    print(f"Date & Time report of {list.upper()}")
    print(f"Abbreviation: {data['abbreviation']}")
    print(f"Client ip: {data['client_ip']}")
    print(f"Date: {data['datetime'][0:10]}")
    print(f"Time: {data['datetime'][11:19]}")
    print(f"Day of the week: {data['day_of_week']+1}")
    print(f"Day of the year: {data['day_of_year']}")
    print(f"TimeZone: {data['timezone']}")
    print(f"UTC offset: UTC{data['utc_offset']}")
    print(f"Week of the month: {data['week_number']}")
elif response.status_code == 404:
    data = response.json()
    if data['error']==(f"unknown location {continent}/{city}"):
        print(f"No data available for {city}")
    else:
        print("Something went wrong!")
else:
    print("Something might be broken")
