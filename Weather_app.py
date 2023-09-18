import customtkinter as ctk
import requests

# Define the OpenWeatherMap API key
api_key = "YOUR_API_KEY"

# Create the root window
root = ctk.CTk()
root.geometry("500x350")

# Define a dictionary to store user credentials (replace with your own authentication logic)
user_credentials = {
    "username": "Mayowa",
    "password": "Test"
}

# Define the weather query function
def get_weather():
    # Clear previous weather data
    temperature_label.configure(text="")
    weather_description_label.configure(text="")
    humidity_label.configure(text="")

    city_name = city_entry.get()  # Get the city name from the entry field
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    # Make a GET request to the OpenWeatherMap API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        
        # Update weather labels with the retrieved data
        temperature_label.configure(text=f"Temperature: {temperature} degrees Celsius")
        weather_description_label.configure(text=f"Weather description: {weather_description}")
        humidity_label.configure(text=f"Humidity: {humidity}%")
    else:
        result_label.configure(text="An error occurred while fetching the weather data.")

# Define the login function
def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == user_credentials["username"] and entered_password == user_credentials["password"]:
        # Successful login, enable the weather query controls
        weather_button.configure(state=ctk.NORMAL)
        result_label.configure(text="Login successful. You can now get weather information.")
    else:
        result_label.configure(text="Login failed. Please check your credentials.")

# Create a frame and pack it into the root window
frame = ctk.CTkFrame(root)
frame.pack()

# Create a label, username entry, password entry, login button, and result label
label = ctk.CTkLabel(frame, text="Login")
label.pack()

username_entry = ctk.CTkEntry(frame)
username_entry.pack()

password_entry = ctk.CTkEntry(frame, show="*")  # Password is hidden
password_entry.pack()

login_button = ctk.CTkButton(frame, text="Login", command=login)
login_button.pack()

result_label = ctk.CTkLabel(frame, text="")
result_label.pack()

city_entry = ctk.CTkEntry(frame)
city_entry.pack()

# Create labels for weather information
temperature_label = ctk.CTkLabel(frame, text="")
temperature_label.pack()

weather_description_label = ctk.CTkLabel(frame, text="")
weather_description_label.pack()

humidity_label = ctk.CTkLabel(frame, text="")
humidity_label.pack()

# Create a button for weather query (disabled until logged in)
weather_button = ctk.CTkButton(frame, text="Get Weather", command=get_weather, state=ctk.DISABLED)
weather_button.pack()

# Start the main loop for the root window
root.mainloop()
