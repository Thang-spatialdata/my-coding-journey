# ==========================
# Day 18 - index() & count()
# ==========================

# --------------------------
# Part 1 - index()
# --------------------------

subjects = ["GIS", "Python", "SQL"]

print(subjects.index("Python"))

# --------------------------
# Part 2 - count()
# --------------------------

numbers = [1, 2, 1, 3, 1]

print(numbers.count(1))

# --------------------------
# Boss Challenge
# --------------------------

rivers = [
    {"name": "Song Hong", "length": 1149},
    {"name": "Song Da", "length": 910},
    {"name": "Song Luoc", "length": 72}
]

print("\nRiver List:")

for river in rivers:
    print(f"{river['name']}: {river['length']} km")

lengths = []

for river in rivers:
    lengths.append(river["length"])

print("\nLongest river:", max(lengths), "km")
print("Shortest river:", min(lengths), "km")
print("Average length:",
      sum(lengths) / len(lengths), "km")

#---------------------------
# Bonus
#---------------------------

rivers = [
    "Song Hong",
    "Song Da",
    "Song Luoc",
    "Song Hong",
    "Song Thai Binh"
]

count = 0

for river in rivers:
    if river == "Song Hong":
        count += 1

print("Song Hong appears:", count)
