# Exercise 1 - Square Root
import math

print(math.sqrt(49))
print(math.sqrt(81))
print(math.sqrt(100))

# Exercise 2 - Power
import math

print(math.pow(2, 3))
print(math.pow(5, 2))
print(math.pow(10, 2))

# Exercise 3 - Ceiling & Floor
import math

numbers = [3.2, 7.8, 15.1]

for n in numbers:
    print(f"{n} - ceil: {math.ceil(n)} - floor: {math.floor(n)}")
  
# Exercise 4 - Circle Area
import math

r = 5
area = math.pi * r ** 2

print(f"Circle area: {area:.2f}")

# Exercise 5 - Random Numbers
from random import randint

numbers = []

for i in range(5):
    numbers.append(randint(1, 100))

print("Random numbers:", numbers)

# Exercise 6 - Distance Function
import math

def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )

point1 = (0, 0)
point2 = (3, 4)

print(f"Distance: {distance(point1, point2):.2f}")
