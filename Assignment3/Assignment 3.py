# Program Name: Assignment3.py
# Course: IT3883/Section W01
# Student Name: Gustavo Gonzalez
# Assignment Number: Lab2
# Due Date: 06/26/2026
# Purpose: The program is created to convert miles per gallon into kilometers per liter. The user will be 
# 1. https://www.geeksforgeeks.org/python/python-gui-tkinter/ 2.https://www.geeksforgeeks.org/python/create-first-gui-application-using-python-tkinter/ 3. https://www.geeksforgeeks.org/python/python-tkinter-entry-widget/


# Using the tkinter library, the program creates a GUI that allows users to input a value in miles per gallon (MPG) and receive the equivalent value in kilometers per liter.
import tkinter as tk
# Create a function to calculate the conversion from miles per gallon (MPG) to kilometers per liter (Km/L).
def calculate(*args):
    try:
        mpg = float(input_var.get())
        result_var.set(f"{mpg * 0.425143707:.4f} Km/L")
    except ValueError:
        result_var.set("0.00 Km/L" if not input_var.get() else "Invalid Input")
# Creating the live trigger for the input variable to call the calculate function whenever the input changes.
root = tk.Tk()
root.title("Converter")

# Creating both the input and output variables. 
input_var = tk.StringVar()
input_var.trace_add("write", calculate)  # Real-time listener
result_var = tk.StringVar(value="0.00 Km/L")

# Creating the GUI layout with labels, entry boxes, and output display.
tk.Label(root, text="Enter MPG:").pack(pady=(10, 0))
input_box = tk.Entry(root, textvariable=input_var)
input_box.pack(pady=5)

# Creating the output label to display the result of the conversion. 
output_label = tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold"))
output_label.pack(pady=10)

root.mainloop()