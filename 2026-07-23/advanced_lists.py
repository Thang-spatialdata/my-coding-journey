# Day 16 - Advanced List Methods

# =========================
# 1. extend()
# =========================
subjects = ["Python", "SQL"]
new_subjects = ["GIS", "English"]

subjects.extend(new_subjects)

print(subjects)

# =========================
# 2. insert()
# =========================
numbers = [5, 15, 25]

numbers.insert(1, 10)

print(numbers)

# =========================
# 3. pop()
# =========================
numbers.pop()

print(numbers)

# =========================
# 4. index()
# =========================
cities = [
    "Hung Yen",
    "Ha Noi",
    "Hung Yen",
    "Nam Dinh"
]

print(cities.index("Hung Yen"))

# =========================
# 5. count()
# =========================
print(cities.count("Hung Yen"))

# =========================
# Boss Challenge
# =========================
rivers = [
    "Song Hong",
    "Song Đa"
]

rivers.append("Sông Thái Bình")

rivers.extend([
    "Song Luoc",
    "Song Đuong"
])

for river in rivers:
    print(river)

print("Total:", len(rivers))
