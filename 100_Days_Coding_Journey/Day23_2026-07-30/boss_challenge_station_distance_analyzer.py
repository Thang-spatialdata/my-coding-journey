import math

stations = [
    ("HY01", (20.65, 106.05)),
    ("HY02", (20.70, 106.10)),
    ("HY03", (20.72, 106.15))
]

center = (20.60, 106.00)
cx, cy = center

max_dist = -1
farthest_station = ""

print("=== STATION LIST ===")

for name, (x, y) in stations:
    print(f"Station: {name} | Coordinates: ({x}, {y})")

    distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    print(f"{name} distance from center: {distance:.2f}")

    if distance > max_dist:
        max_dist = distance
        farthest_station = name

print("\n=== REPORT ===")
print(f"Farthest station: {farthest_station}")
print(f"Distance: {max_dist:.2f}")
