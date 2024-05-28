import requests
import ipinfo

api_key = "bb9c70e60e3ee7e5cc6e740c9b1fc488"
ipinfo_token = "9335f66b2ee0dc"
language = "hr"

def get_local_weather():
    try:
        handler = ipinfo.getHandler(ipinfo_token)
        details = handler.getDetails()
        
        latitude = details.latitude
        longitude = details.longitude

        local_weather=""

        local_weather+=f"Lokacija: {details.city}, {details.region}, {details.country}\n"

        url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric&lang={language}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            local_weather+="Trenutno vrijeme:\n"
            local_weather+=f"Sažetak: {weather}\n"
            local_weather+=f"Temperatura: {temperature} °C\n"
            local_weather+=f"Vlaga: {humidity} %\n"
            local_weather+=f"Vjetar: {wind_speed} m/s\n"
            return local_weather
        else:
            return f"Neuspješno dohvaćanje podataka o vremenu: {data.get("Poruka", "Nepoznati error")}"
        
    except Exception as e:
        return f"Došlo je do pgreške: {e}"


