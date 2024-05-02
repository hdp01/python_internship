import requests

API_KEY = "e31bbb7caa8bc5edda7c60044fb628d7"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather_data(city_name):
    # Complete URL for the API request
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
    # Send a GET request to the API
    response = requests.get(complete_url)
    # Convert the response to JSON format
    weather_data = response.json()
    return weather_data

def display_weather_data(weather_data):
    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        temperature = main_data["temp"] - 273.15  # Convert temperature from Kelvin to Celsius
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_description = weather_data["weather"][0]["description"]

        print(f"Temperature: {temperature:.1f} °C")
        print(f"Atmospheric pressure: {pressure} hPa")
        print(f"Humidity: {humidity} %")
        print(f"Weather description: {weather_description}")
    else:
        print("City not found.")

def get_user_input():
    city_name = input("Enter city name: ")
    return city_name

def main():
    city_name = get_user_input()

    weather_data = get_weather_data(city_name)

    display_weather_data(weather_data)

if __name__ == "__main__":
    main()