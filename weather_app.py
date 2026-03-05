import tkinter as tk
from tkinter import messagebox
import random

def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    # Fake weather data (NO INTERNET REQUIRED)
    temperature = random.randint(20, 40)
    humidity = random.randint(40, 90)
    condition = random.choice([
        "Sunny", "Cloudy", "Rainy", "Windy", "Partly Cloudy"
    ])

    # 🔹 Output Window (NEW PAGE)
    output = tk.Toplevel(root)
    output.title("Weather Result")
    output.geometry("400x300")

    tk.Label(
        output,
        text="Weather Report",
        font=("Arial", 20, "bold")
    ).pack(pady=15)

    tk.Label(
        output,
        text=f"City: {city.title()}",
        font=("Arial", 14)
    ).pack(pady=5)

    tk.Label(
        output,
        text=f"Temperature: {temperature} °C",
        font=("Arial", 14)
    ).pack(pady=5)

    tk.Label(
        output,
        text=f"Humidity: {humidity} %",
        font=("Arial", 14)
    ).pack(pady=5)

    tk.Label(
        output,
        text=f"Condition: {condition}",
        font=("Arial", 14)
    ).pack(pady=5)


# 🔹 Main Window
root = tk.Tk()
root.title("Basic Weather App")
root.geometry("400x250")

tk.Label(
    root,
    text="Basic Weather App",
    font=("Arial", 18, "bold")
).pack(pady=15)

tk.Label(
    root,
    text="Enter City Name",
    font=("Arial", 12)
).pack()

city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12),
    command=get_weather
).pack(pady=20)

root.mainloop()