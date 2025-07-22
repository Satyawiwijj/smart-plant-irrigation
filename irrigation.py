import tkinter as tk
from tkinter import messagebox
import random

# Moisture thresholds for different plants
PLANT_THRESHOLDS = {
    "Cactus": 20,
    "Tulsi": 40,
    "Tomato": 60
}

def simulate_moisture():
    return random.randint(0, 100)

def check_moisture():
    plant = selected_plant.get()
    if plant not in PLANT_THRESHOLDS:
        messagebox.showwarning("Select Plant", "Please select a plant type.")
        return
    
    threshold = PLANT_THRESHOLDS[plant]
    moisture = simulate_moisture()
    
    result_label.config(text=f"Simulated Moisture Level: {moisture}")

    if moisture < threshold:
        messagebox.showinfo("Irrigation Needed", f"Moisture is low for {plant}.\nWater the plant.")
    else:
        messagebox.showinfo("No Irrigation Needed", f"Moisture is sufficient for {plant}.")

# GUI setup
root = tk.Tk()
root.title("Smart Plant Irrigation System")
root.geometry("400x300")
root.configure(bg="#e9f5e1")

# Title
title = tk.Label(root, text="🌱 Smart Plant Irrigation System", font=("Helvetica", 16, "bold"), bg="#e9f5e1")
title.pack(pady=20)

# Plant dropdown
selected_plant = tk.StringVar()
selected_plant.set("Select Plant")

plant_menu = tk.OptionMenu(root, selected_plant, *PLANT_THRESHOLDS.keys())
plant_menu.config(width=20, font=("Helvetica", 12))
plant_menu.pack(pady=10)

# Check button
check_button = tk.Button(root, text="Check Moisture Level", command=check_moisture, bg="#4caf50", fg="white", font=("Helvetica", 12), width=20)
check_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#e9f5e1")
result_label.pack(pady=10)

# Run the app
root.mainloop()
