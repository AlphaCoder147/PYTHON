import requests

API_KEY = "bd42fe4d6d72c20ffd80daec8e0171b9"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)
if response.status_code==200:
    data=response.json
    weather=data['weather'][0]['description']
    temperature=round(data["main"]["temp"]-273.15,2)
    
    print("Weather: ",weather)
    print("Temperature: ",temperature,"Celcius")
    
else:
    print("An error occured")    