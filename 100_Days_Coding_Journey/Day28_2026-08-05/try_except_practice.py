# Day 28 - Try / Except Practice

# Exercise 1
try:
    value = float("25.5")
    print(f"Converted value: {value}")
except ValueError:
    print("Cannot convert")

# Exercise 2
try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")

# Exercise 3
station = {"name": "HY01"}

try:
    print(station["temperature"])
except KeyError:
    print("Temperature data is missing")
