# Program Name: Assignment5.py (use the name the program is saved as) 

# Course: IT3883/Section W01 

# Student Name: Gustavo Gonzalez

# Assignment Number: Lab5 

# Due Date: 07/17/2026 

# Purpose: What does the program do (in a few sentences)? The program reads daily weather data from a text file, stores it in a SQLite database, and calculates the average temperature for specific days of the week which is Sunday and Thursday in this instance.

# List Specific resources used to complete the assignment. 1. https://www.google.com/search?q=sqlite+3+database+geeks+for+geeks&sca_esv=f07c4d704701945c&sxsrf=APpeQnuQCTC8INl8bal2vLo5HqHmRKKtuw%3A1784142998592&ei=ltxXar3WI8iHp84PnLH1gQs&biw=1022&bih=1016&oq=sqlite+3+database+geeks+&gs_lp=Egxnd3Mtd2l6LXNlcnAiGHNxbGl0ZSAzIGRhdGFiYXNlIGdlZWtzICoCCAAyBxAhGAoYoAEyBRAhGKsCMgUQIRirAkjrKlCVDVjDIHABeAGQAQKYAXugAcQEqgEDMS40uAEDyAEA-AEBmAIEoALfAsICChAAGEcY1gQYsAPCAgsQABiABBiKBRiRAsICBhAAGBYYHsICCBAAGBYYHhgKwgIFECEYnwWYAwCIBgGQBgiSBwMxLjOgB-sSsgcDMC4zuAfcAsIHBTAuMy4xyAcIgAgB&sclient=gws-wiz-serp 2. https://docs.python.org/3/library/sqlite3.html 3. https://stackoverflow.com/questions/55832852/python-program-inserting-txt-file-to-sqlite3-database

import sqlite3
# Creating a connection to the database
conn = sqlite3.connect("daily_weather_data.db")
cursor = conn.cursor()
# Creating the table to store daily weather data
cursor.execute("Drop TABLE IF EXISTS daily_weather_data")
cursor.execute(
    """
    CREATE TABLE daily_weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT,
        Temperature_Value REAL
    )
"""
)
# Inserting data from the text file into the database
with open("Assignment5input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            day, temp = parts[0], float(parts[1])
            cursor.execute(
                "INSERT INTO daily_weather_data (Day_Of_Week, Temperature_Value) VALUES (?, ?)",
                (day, temp)
        )
conn.commit()
# Calculating and printing the average temperature for Sunday and Thursday
for day in ["Sunday", "Thursday"]:
    cursor.execute(
        "SELECT AVG(Temperature_Value) FROM daily_weather_data WHERE Day_Of_Week = ?",
        (day,),
    )
    avg_temp = cursor.fetchone()[0] or 0
    print(f"Average temperature for {day}: {avg_temp:.2f}")
conn.close()