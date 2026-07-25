# Practice 1

subjects = ["Python", "GIS", "SQL"]

for index, subject in enumerate(subjects, start=1):
    print(index, subject)

print()

# Practice 2

numbers = [10, 20, 30, 40]

for index, number in enumerate(numbers, start=1):
    print(f"Phần tử thứ {index} là {number}")

print()

# Practice 3

cities = ["Hưng Yên", "Hà Nội", "Nam Định"]

for index, city in enumerate(cities, start=1):
    if index % 2 == 0:
        print(city)
