import math

center = (0, 0)

stations = {
    "HY01": (3, 4),
    "HY02": (1, 1),
    "HY03": (6, 8)
}

def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )

nearest_station = ""
min_distance = float("inf")

for name, coords in stations.items():
    d = distance(center, coords)
    print(f"{name}: {d:.2f}")

    if d < min_distance:
        min_distance = d
        nearest_station = name

print("\n=== Nearest Station Report ===")
print(f"Nearest station: {nearest_station}")
print(f"Distance: {min_distance:.2f}")
