import json

raw_json_lines = [
    '{"name": "HY01", "temp": 28}',
    '{"name": "HY02", "temp": 33}',
    '{"name": "HY03"}',
    'not valid json',
    '{"name": "HY04", "temp": 19}'
]

json_error_count = 0
key_error_count = 0
valid_records = []

for line in raw_json_lines:
    try:
        data = json.loads(line)
        temp_value = data["temp"]
        valid_records.append(data)

    except json.JSONDecodeError:
        json_error_count += 1

    except KeyError:
        key_error_count += 1

final_stations = {
    record["name"]: record["temp"]
    for record in valid_records
    if record["temp"] >= 25
}

print(f"Resulting dictionary: {final_stations}")
print(f"Number of JSON decode errors: {json_error_count}")
print(f"Number of missing-temperature errors: {key_error_count}")
