# #Advanced BMI Calculator with UI and data storage
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

# File to store BMI records
FILE_NAME = "bmi_records.csv"

def save_to_csv(weight, height, bmi, category):
    """Save BMI data to a CSV file."""
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), weight, height, f"{bmi:.2f}", category])

def calculate_bmi():
    
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and height must be positive values.")
            return
        
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "#3498db"  # Blue
        elif 18.5 <= bmi <= 24.9:
            category = "Normal Weight"
            color = "#2ecc71"  # Green
        elif 25 <= bmi <= 29.9:
            category = "Overweight"
            color = "#f1c40f"  # Yellow
        else:
            category = "Obese"
            color = "#e74c3c"  # Red

        # Display result
        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}", foreground=color)

        # Save data to CSV
        save_to_csv(weight, height, bmi, category)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for weight and height.")

def view_records():
    
    try:
        with open(FILE_NAME, mode="r") as file:
            records = file.readlines()
            if not records:
                messagebox.showinfo("No Records", "No previous BMI records found.")
                return

        # Display records in a new window
        record_window = tk.Toplevel(root)
        record_window.title("BMI Records")
        record_window.geometry("400x300")

        text_area = tk.Text(record_window, wrap="word", font=("Arial", 12))
        text_area.pack(expand=True, fill="both")

        text_area.insert("end", "Date & Time\tWeight (kg)\tHeight (m)\tBMI\tCategory\n")
        text_area.insert("end", "-" * 60 + "\n")

        for record in records:
            text_area.insert("end", record)

    except FileNotFoundError:
        messagebox.showinfo("No Records", "No previous BMI records found.")

def plot_bmi_trend():
    
    if not os.path.exists(FILE_NAME):
        messagebox.showinfo("No Data", "No BMI records found. Calculate BMI first!")
        return

    dates, bmi_values = [], []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                dates.append(datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S"))
                bmi_values.append(float(row[3]))
            except (ValueError, IndexError):
                continue  # Skip invalid entries

    if not dates or not bmi_values:
        messagebox.showinfo("No Data", "Not enough data to plot a graph.")
        return

    # Plot the BMI trend
    plt.figure(figsize=(8, 5))
    plt.plot(dates, bmi_values, marker='o', linestyle='-', color='b', label="BMI Trend")
    plt.xlabel("Date")
    plt.ylabel("BMI Value")
    plt.title("BMI Trend Over Time")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.show()


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x500")
root.configure(bg="#ecf0f1")

title_label = ttk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold"), background="#ecf0f1")
title_label.pack(pady=10)

input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

ttk.Label(input_frame, text="Weight (kg):", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
weight_entry = ttk.Entry(input_frame, font=("Arial", 12))
weight_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Height (m):", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
height_entry = ttk.Entry(input_frame, font=("Arial", 12))
height_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = ttk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=5)

view_button = ttk.Button(root, text="View Records", command=view_records)
view_button.pack(pady=5)

graph_button = ttk.Button(root, text="View BMI Trend", command=plot_bmi_trend)
graph_button.pack(pady=5)

result_label = ttk.Label(root, text="", font=("Arial", 14, "bold"), background="#ecf0f1")
result_label.pack(pady=10)

root.mainloop()


# #Advanced BMI Calculator with UI and data storage
# import tkinter as tk
# from tkinter import ttk, messagebox

# def calculate_bmi():
#     try:
#         weight = float(weight_entry.get())
#         height = float(height_entry.get())

#         if weight <= 0 or height <= 0:
#             messagebox.showerror("Invalid Input", "Weight and height must be positive values.")
#             return
        
#         bmi = weight / (height ** 2)

#         if bmi < 18.5:
#             category = "Underweight"
#             color = "#3498db"  # Blue
#         elif 18.5 <= bmi <= 24.9:
#             category = "Normal Weight"
#             color = "#2ecc71"  # Green
#         elif 25 <= bmi <= 29.9:
#             category = "Overweight"
#             color = "#f1c40f"  # Yellow
#         else:
#             category = "Obese"
#             color = "#e74c3c"  # Red

#         result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}", foreground=color)

#     except ValueError:
#         messagebox.showerror("Input Error", "Please enter valid numeric values for weight and height.")

# root = tk.Tk()
# root.title("BMI Calculator")
# root.geometry("350x400")
# root.configure(bg="#ecf0f1") 


# title_label = ttk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold"), background="#ecf0f1")
# title_label.pack(pady=10)

# input_frame = ttk.Frame(root)
# input_frame.pack(pady=10)


# ttk.Label(input_frame, text="Weight (kg):", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
# weight_entry = ttk.Entry(input_frame, font=("Arial", 12))
# weight_entry.grid(row=0, column=1, padx=5, pady=5)

# ttk.Label(input_frame, text="Height (m):", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
# height_entry = ttk.Entry(input_frame, font=("Arial", 12))
# height_entry.grid(row=1, column=1, padx=5, pady=5)

# calculate_button = ttk.Button(root, text="Calculate BMI", command=calculate_bmi)
# calculate_button.pack(pady=10)

# result_label = ttk.Label(root, text="", font=("Arial", 14, "bold"), background="#ecf0f1")
# result_label.pack(pady=10)

# root.mainloop()






# Basic BMI Calculator

# def bmi_calculation(weight,height):

#     if weight <= 0 or height <= 0:
#         return "Invalid value!, The vale must be positve."
    
#     bmi = weight / (height ** 2)
    
#     if bmi < 18.5:
#         category = "Underweight"
#     elif 18.5 <= bmi <= 24.9: 
#         category = "Normal Weight"
#     elif 25 <= bmi <= 29.9:  
#         category = "Overweight"
#     else:
#         category = "Obese"

#     return f"The BMI Value is {bmi:.2f}, Which falls under the category of {category}."




# weight = float(input("Enter your weight in kg's"))
# height = float(input("Enter your height in meters"))

# print(bmi_calculation(weight,height))