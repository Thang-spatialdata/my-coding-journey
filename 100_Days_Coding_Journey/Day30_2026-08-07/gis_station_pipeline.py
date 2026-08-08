import json
import math

raw_reports = [
    '{"station": "HY01", "temp": "28", "lat": 21.03, "lon": 105.85}',
    '{"station": "HY02", "temp": "31", "lat": 20.85, "lon": 106.68}',
    '{"station": "HY01", "temp": "28", "lat": 21.03, "lon": 105.85}',
    'invalid entry, skip me',
    '{"station": "hy03", "temp": "abc", "lat": 20.60, "lon": 106.20}',
    '{"station": "HY04", "lat": 20.95, "lon": 106.05}',
    '{"station": "HY05", "temp": "35", "lat": 20.50, "lon": 105.90}'
]

center = (21.0, 106.0)

invalid_json_count = 0
duplicate_count = 0
missing_temp_count = 0
invalid_temp_count = 0
seen_stations = set()
clean_records = []

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

for entry in raw_reports:
    try:
        data = json.loads(entry)
    except json.JSONDecodeError:
        invalid_json_count += 1
        continue

    station_name = data.get("station", "").upper()
    data["station"] = station_name

    if station_name in seen_stations:
        duplicate_count += 1
        continue
    seen_stations.add(station_name)

    if "temp" not in data:
        missing_temp_count += 1
        continue

    try:
        data["temp"] = float(data["temp"])
    except ValueError:
        invalid_temp_count += 1
        continue

    station_coords = (data["lat"], data["lon"])
    data["distance_from_center"] = distance(center, station_coords)
    clean_records.append(data)

with open("clean_report.json", "w") as file:
    json.dump(clean_records, file)

valid_records_count = len(clean_records)

hottest_station = clean_records[0]
for record in clean_records:
    if record["temp"] > hottest_station["temp"]:
        hottest_station = record

nearest_station = clean_records[0]
for record in clean_records:
    if record["distance_from_center"] < nearest_station["distance_from_center"]:
        nearest_station = record

print("\n=== GIS STATION PIPELINE REPORT ===")
print(f"Total raw entries: {len(raw_reports)}")
print(f"Invalid JSON: {invalid_json_count}")
print(f"Duplicates skipped: {duplicate_count}")
print(f"Missing temperature: {missing_temp_count}")
print(f"Invalid temperature: {invalid_temp_count}")
print(f"Valid records: {valid_records_count}")
print(f"Hottest station: {hottest_station['station']} ({hottest_station['temp']}°C)")
print(f"Nearest to center: {nearest_station['station']}\n")
