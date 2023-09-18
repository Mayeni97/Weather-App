import requests

# Define the API key
api_key = "YOUR_API_KEY"

# Get the city name from the user
city_name = input("Enter the city name: ")

# Construct the URL for the OpenWeatherMap API
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)

# Make a GET request to the OpenWeatherMap API
response = requests.get(url)

# Check the status code of the response
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    # Get the temperature from the JSON data
    temperature = data["main"]["temp"]

    # Get the weather description from the JSON data
    weather_description = data["weather"][0]["description"]

    # Get the humidity from the JSON data
    humidity = data["main"]["humidity"]

    # Print the temperature, weather description, and humidity to the console
    print("Temperature: {} degrees Celsius".format(temperature))
    print("Weather description: {}".format(weather_description))
    print("Humidity: {}%".format(humidity))

else:
    # Print an error message to the console
    print("An error occurred while fetching the weather data.")