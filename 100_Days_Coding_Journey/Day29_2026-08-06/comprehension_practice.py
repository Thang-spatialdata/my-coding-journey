# Day 29 - Comprehension Practice

# Exercise 1
temperatures = [28, 31, 25, 35, 20]
adjusted = [temp + 2 for temp in temperatures]
print(f"Adjusted temperatures: {adjusted}")

# Exercise 2
cold = [temp for temp in temperatures if temp < 25]
print(f"Cold temperatures: {cold}")

# Exercise 3
stations = ["HY01", "HY02", "HY03"]
temps = [28, 31, 25]

station_temps = {name: temp for name, temp in zip(stations, temps)}
print(f"Station dictionary: {station_temps}")
