import requests

def get_weather(location):
    api_key = '8b88caa2961db764c6dcff82106c9812'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None