# Day 21 - Set in Python
# Basic Set operations

print("=== Python Set Practice ===")

# Creating a Set
stations = {
    "HY01",
    "HY02",
    "HY03"
}

print("Original stations:")
print(stations)

# Removing duplicate data
station_list = [
    "HY01",
    "HY02",
    "HY01",
    "HY03",
    "HY02"
]

unique_stations = set(station_list)

print("\nUnique stations:")
for station in unique_stations:
    print(station)


# Adding a new station
unique_stations.add("HY04")

print("\nAfter adding HY04:")
print(unique_stations)

# Removing a station
unique_stations.remove("HY02")

print("\nAfter removing HY02:")
print(unique_stations)

# Set operations

district_A = {
    "HY01",
    "HY02",
    "HY03"
}

district_B = {
    "HY03",
    "HY04",
    "HY05"
}

print("\nUnion (All stations):")
print(district_A | district_B)

print("\nIntersection (Common stations):")
print(district_A & district_B)

print("\nDifference (Only in district A):")
print(district_A - district_B)
