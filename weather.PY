import tkinter as tk
import requests
import time

def getWeather(event):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=5823bbfc7261fca73dba97de521af92a"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
canvas.configure(bg="#0f172a")

f = ("Poppins", 15)
t = ("Poppins", 35, "bold")

textfield = tk.Entry(
    canvas,
    font=t,
    bg="#1e293b",
    fg="white",
    insertbackground="white",
    relief="flat",
    justify="center"
)
textfield.pack(pady=30, ipadx=10, ipady=10)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(
    canvas,
    font=t,
    bg="#0f172a",
    fg="#38bdf8"
)
label1.pack()
label2 = tk.Label(
    canvas,
    font=f,
    bg="#0f172a",
    fg="white",
    justify="left"
)
label2.pack()
canvas.mainloop()
