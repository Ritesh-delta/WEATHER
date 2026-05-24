import tkinter as tk
from tkinter import messagebox
import requests
import time

# ---------------- API KEY ---------------- #
API_KEY = "5823bbfc7261fca73dba97de521af92a"

# ---------------- FUNCTIONS ---------------- #
def get_weather(event=None):
    city = textfield.get().strip()

    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    try:
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

        json_data = requests.get(api).json()

        if json_data.get("cod") != 200:
            messagebox.showerror("Error", "City not found")
            return

        # Weather Data
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description'].title()

        temp = int(json_data['main']['temp'] - 273.15)
        feels_like = int(json_data['main']['feels_like'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)

        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        sunrise = time.strftime(
            '%I:%M %p',
            time.localtime(json_data['sys']['sunrise'])
        )

        sunset = time.strftime(
            '%I:%M %p',
            time.localtime(json_data['sys']['sunset'])
        )

        # Weather Icons
        weather_icons = {
            "Clear": "☀️",
            "Clouds": "☁️",
            "Rain": "🌧️",
            "Drizzle": "🌦️",
            "Thunderstorm": "⛈️",
            "Snow": "❄️",
            "Mist": "🌫️",
            "Haze": "🌫️",
            "Fog": "🌫️"
        }

        icon = weather_icons.get(condition, "🌍")

        # Main Display
        weather_label.config(
            text=f"{icon}  {temp}°C"
        )

        city_label.config(
            text=f"{city.title()}"
        )

        condition_label.config(
            text=f"{description}"
        )

        details = (
            f"Feels Like : {feels_like}°C\n"
            f"Min Temp   : {min_temp}°C\n"
            f"Max Temp   : {max_temp}°C\n"
            f"Humidity   : {humidity}%\n"
            f"Pressure   : {pressure} hPa\n"
            f"Wind Speed : {wind} m/s\n"
            f"Sunrise    : {sunrise}\n"
            f"Sunset     : {sunset}"
        )

        details_label.config(text=details)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("Modern Weather App")
root.geometry("500x650")
root.resizable(False, False)
root.configure(bg="#0f172a")  # Dark background

# ---------------- FONTS ---------------- #
TITLE_FONT = ("Poppins", 30, "bold")
TEMP_FONT = ("Poppins", 48, "bold")
DETAIL_FONT = ("Poppins", 14)
ENTRY_FONT = ("Poppins", 18)

# ---------------- TOP FRAME ---------------- #
top_frame = tk.Frame(root, bg="#0f172a")
top_frame.pack(pady=20)

title = tk.Label(
    top_frame,
    text="Weather App",
    font=TITLE_FONT,
    fg="white",
    bg="#0f172a"
)
title.pack()

# ---------------- SEARCH BOX ---------------- #
search_frame = tk.Frame(root, bg="#0f172a")
search_frame.pack(pady=20)

textfield = tk.Entry(
    search_frame,
    font=ENTRY_FONT,
    width=20,
    justify="center",
    relief="flat",
    bg="#1e293b",
    fg="white",
    insertbackground="white"
)
textfield.grid(row=0, column=0, padx=10, ipady=10)

textfield.focus()
textfield.bind('<Return>', get_weather)

search_btn = tk.Button(
    search_frame,
    text="Search",
    font=("Poppins", 14, "bold"),
    bg="#38bdf8",
    fg="white",
    relief="flat",
    padx=15,
    pady=8,
    cursor="hand2",
    command=get_weather
)

search_btn.grid(row=0, column=1)

# ---------------- WEATHER CARD ---------------- #
card = tk.Frame(
    root,
    bg="#1e293b",
    bd=0,
    relief="flat"
)
card.pack(padx=30, pady=20, fill="both", expand=True)

# City Name
city_label = tk.Label(
    card,
    text="Enter City Name",
    font=("Poppins", 24, "bold"),
    fg="white",
    bg="#1e293b"
)
city_label.pack(pady=(30, 10))

# Temperature
weather_label = tk.Label(
    card,
    text="🌤️  --°C",
    font=TEMP_FONT,
    fg="#38bdf8",
    bg="#1e293b"
)
weather_label.pack()

# Condition
condition_label = tk.Label(
    card,
    text="Weather Condition",
    font=("Poppins", 18),
    fg="#cbd5e1",
    bg="#1e293b"
)
condition_label.pack(pady=10)

# Divider
divider = tk.Frame(card, bg="#334155", height=2)
divider.pack(fill="x", padx=40, pady=15)

# Details
details_label = tk.Label(
    card,
    text="Weather details will appear here",
    font=DETAIL_FONT,
    fg="white",
    bg="#1e293b",
    justify="left"
)
details_label.pack(pady=10)

# ---------------- FOOTER ---------------- #
footer = tk.Label(
    root,
    text="Made with Tkinter ❤️",
    font=("Poppins", 10),
    fg="#94a3b8",
    bg="#0f172a"
)
footer.pack(pady=10)

# ---------------- RUN APP ---------------- #
root.mainloop()