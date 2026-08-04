import json


# Practice 1 - Convert dict to JSON
station = {
    "name": "HY01",
    "temp": 28,
    "rainfall": 120
}

json_text = json.dumps(station)
print(json_text)


# Practice 2 - Write JSON file
with open("hy03.json", "w") as f:
    json.dump(station, f)


# Practice 3 - Read JSON file
with open("hy03.json", "r") as f:
    loaded_station = json.load(f)

print(loaded_station)


# Practice 4 - Read specific value
print(f"Temperature: {loaded_station['temp']}°C")
