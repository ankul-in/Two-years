import requests 
import datetime as dt


city_name = 'New Delhi'
API_Key = 'yourApiHere'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

response = requests.get(url)
if response.status_code == 200:
    print('yes, we hit')
    data = response.json()
    print('weather is ', data['weather'][0]['description'])
    print(data['main']['temp'])
else:
    print(f"Error: {response.status_code} - {response.text}")