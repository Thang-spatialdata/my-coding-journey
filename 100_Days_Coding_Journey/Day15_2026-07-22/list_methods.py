# Day 15 - List Methods

# Exercise 1: append()
subjects = ["Python", "SQL"]
subjects.append("GIS")
print(subjects)

print()

# Exercise 2: remove()
numbers = [10, 20, 30, 40]
numbers.remove(20)
print(numbers)

print()

# Exercise 3: len() and in
cities = ["Hung Yen", "Ha Noi", "Hai Phong"]
print(len(cities))
print("Nam Dinh" in cities)

print()

# Boss Challenge
stations = ["Station A", "Station B"]

stations.append("Station C")
stations.append("Station D")

for station in stations:
    print(station)

print("Total:", len(stations))
