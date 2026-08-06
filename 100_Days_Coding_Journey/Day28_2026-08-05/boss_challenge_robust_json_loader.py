import json

# Create sample files
with open("station_HY01.json", "w") as file:
    json.dump({"name": "HY01", "temp": 28}, file)

with open("station_HY02.json", "w") as file:
    json.dump({"name": "HY02"}, file)

station_files = [
    "station_HY01.json",
    "station_HY02.json",
    "station_HY03.json"
]

valid_temps = []
success_count = 0
error_count = 0

for file_name in station_files:
    try:
        with open(file_name, "r") as file:
            data = json.load(file)

        temp = data["temp"]
        station_name = data["name"]

        print(f"{station_name}: {temp}°C")

        valid_temps.append(temp)
        success_count += 1

    except FileNotFoundError:
        print(f"File not found: {file_name}")
        error_count += 1

    except KeyError:
        print(f"Missing temperature data: {file_name}")
        error_count += 1

if valid_temps:
    avg_temp = sum(valid_temps) / len(valid_temps)
else:
    avg_temp = 0

print("\n=== REPORT ===")
print(f"Error files: {error_count}")
print(f"Successful files: {success_count}")
print(f"Average temperature: {avg_temp:.2f}°C")
