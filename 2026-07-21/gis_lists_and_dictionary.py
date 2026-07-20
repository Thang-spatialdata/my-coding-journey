# Day 14 - Python Lists & GIS Practice

# Exercise 1: Dictionary
city = {
    "name": "Hung Yen",
    "population": 125000,
    "area": 930.2
}

print("City:", city["name"])
print("Area:", city["area"])


# Exercise 2: Lists + for loop
cities = [
    "Hung Yen",
    "Ha Noi",
    "Hai Phong",
    "Nam Dinh"
]

for city in cities:
    print(f"I want to survey {city}")


# Exercise 3: Function
def population_density(population, area):
    return population / area

print(population_density(125000, 930.2))


# Boss Challenge
province = {
    "name": "Hung Yen",
    "districts": 10,
    "population": 1200000
}

for key, value in province.items():
    print(f"{key}: {value}")
