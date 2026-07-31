# Boss Challenge - GIS Observation Log System
from datetime import datetime
import random

stations = ['HY01', 'HY02', 'HY03', 'HY04', 'HY05']
logs = []
hot_stations = []

# Generate records
for st in stations:
    temp = random.randint(25, 35)
    log_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    record = {
        'name': st,
        'temperature': temp,
        'time': log_time
    }
    logs.append(record)
    
    if temp >= 30:
        hot_stations.append(st)

# Print all logs
print("=== LOG RECORDS ===")
for log in logs:
    print(log)

# Calculate statistics
temps = [log['temperature'] for log in logs]
max_temp = max(temps)
min_temp = min(temps)
avg_temp = sum(temps) / len(temps)

# Select emergency station
emergency_station = random.choice(stations)
report_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Final Report
print("\n=== OBSERVATION REPORT ===")
print(f"Max temperature: {max_temp}°C")
print(f"Min temperature: {min_temp}°C")
print(f"Average temperature: {avg_temp:.2f}°C")
print(f"Hot stations count: {len(hot_stations)}")
print(f"Emergency inspection station: {emergency_station}")
print(f"Report generation time: {report_time}")
  
