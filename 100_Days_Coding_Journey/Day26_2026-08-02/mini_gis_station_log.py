stations = {
    "HY01": 28,
    "HY02": 31,
    "HY03": 25,
    "HY04": 35
}

# Write station data
with open("station_log.txt", "w") as f:
    for name, temp in stations.items():
        f.write(f"{name}, {temp}\n")

# Read file again and calculate average
temp_list = []

with open("station_log.txt", "r") as f:
    for line in f:
        clean = line.strip()
        name, temp = clean.split(", ")
        temp_list.append(int(temp))

if temp_list:
    average_temp = sum(temp_list) / len(temp_list)
    print("=== Station Log Report ===")
    print(f"Average temperature: {average_temp:.2f}°C")
else:
    print("No temperature data")
