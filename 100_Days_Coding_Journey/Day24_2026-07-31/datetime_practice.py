# Exercise 1 - Format Specific Date
from datetime import datetime

survey_time = datetime(2026, 3, 20, 8, 0)
print(survey_time.strftime("%d/%m/%Y"))

# Exercise 2 - Days Between Dates
from datetime import datetime

t1 = datetime(2026, 1, 1)
t2 = datetime(2026, 6, 15)
delta = t2 - t1

print(f"Days between: {delta.days}")

# Exercise 3 - Current Year and Month
from datetime import datetime

now = datetime.now()
print(f"Year: {now.year}, Month: {now.month}")
