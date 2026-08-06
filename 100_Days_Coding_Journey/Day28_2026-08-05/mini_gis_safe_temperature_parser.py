# Mini GIS — Safe Temperature Parser

raw_temperatures = ["28", "31", "abc", "25", "", "35"]

valid_temps = []
skipped_count = 0

for item in raw_temperatures:
    try:
        temp_float = float(item)
        valid_temps.append(temp_float)
    except ValueError:
        skipped_count += 1

if valid_temps:
    avg_temp = sum(valid_temps) / len(valid_temps)
else:
    avg_temp = 0

print(f"Valid values: {len(valid_temps)}")
print(f"Skipped values: {skipped_count}")
print(f"Average temperature: {avg_temp:.2f}°C")
