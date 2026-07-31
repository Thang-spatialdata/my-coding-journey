# Mini GIS - Observation Log
from datetime import datetime

import random

stations = ['HY01', 'HY02', 'HY03']
hot_count = 0

for st in stations:
    temp = random.randint(26, 34)
    time_str = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")
    print(f"{time_str} {st} - {temp}°C")
    
    if temp >= 30:
        hot_count += 1

print(f"Hot stations count: {hot_count}")
