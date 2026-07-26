# =========================
# Day 20 - Practice
# =========================

print("===== Exercise 1 =====")

subjects = [
    "Python",
    "GIS",
    "SQL"
]

days = [
    10,
    15,
    8
]

for subject, day in zip(subjects, days):
    print(f"{subject}: {day}")

print("\n===== Exercise 2 =====")

cities = [
    "Hung Yen",
    "Ha Noi",
    "Hai Phong"
]

population = [
    120000,
    8000000,
    2000000
]

for city, people in zip(cities, population):
    print(f"{city} - {people}")

print("\n===== Exercise 3 =====")

students = [
    "Linh",
    "Nam",
    "An"
]

majors = [
    "GIS",
    "IT",
    "AI"
]

for student, major in zip(students, majors):
    if major ["GIS", "AI"]:
        print(f"{student} - {major}")
