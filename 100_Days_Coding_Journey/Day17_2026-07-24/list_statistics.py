# Day 17 - Sorting and Statistics with Lists

# ==========================
# sort()
# ==========================

numbers = [8, 3, 6, 1, 5]

numbers.sort()

print("Sorted numbers:", numbers)

print()

# ==========================
# sorted()
# ==========================

cities = ["Hung Yen", "Ha Noi", "Hai Phong"]

sorted_cities = sorted(cities)

print("Original list:", cities)
print("Sorted list:", sorted_cities)

print()

# ==========================
# reverse()
# ==========================

letters = ["A", "B", "C", "D"]

letters.reverse()

print("Reversed list:", letters)

print()

# ==========================
# min(), max(), sum()
# ==========================

scores = [75, 90, 88, 95, 80]

print("Minimum:", min(scores))
print("Maximum:", max(scores))
print("Total:", sum(scores))
print("Average:", sum(scores) / len(scores))

print()

# ==========================
# Practice 1
# ==========================

numbers = [12, 8, 20, 5, 15]

numbers.sort()

print(numbers)

print()

# ==========================
# Practice 2
# ==========================

cities = ["Ha Noi", "Hai Phong", "Hung Yen"]

cities.reverse()

print(cities)

print()

# ==========================
# Practice 3
# ==========================

def total(numbers):
    return sum(numbers)

values = [10, 20, 30]

print(total(values))

print()

# ==========================
# Boss Challenge
# ==========================

stations = [
    {"name": "HY01", "temperature": 30},
    {"name": "HY02", "temperature": 27},
    {"name": "HY03", "temperature": 32},
    {"name": "HY04", "temperature": 29}
]

print("Weather Stations:")

for station in stations:
    print(f"Station {station['name']}: {station['temperature']}°C")

temperatures = []

for station in stations:
    temperatures.append(station["temperature"])

print("Highest temperature:", max(temperatures))
print("Lowest temperature:", min(temperatures))
print("Average temperature:", sum(temperatures) / len(temperatures))
