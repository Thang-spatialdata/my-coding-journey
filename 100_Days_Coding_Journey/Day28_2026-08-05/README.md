# Day 28 - Try / Except & Error Handling

## 📚 What I Learned

Today I learned:

- `try`
- `except`
- `ValueError`
- `FileNotFoundError`
- `KeyError`
- `finally`
- Handling invalid GIS-style data safely

---

## 💻 Practice

### ✔ Convert string to float safely

```python
try:
    value = float("25.5")
    print(value)
except ValueError:
    print("Cannot convert")
```

### ✔ Handle missing file

```python
try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

### ✔ Handle missing dictionary key

```python
station = {"name": "HY01"}

try:
    print(station["temperature"])
except KeyError:
    print("Temperature data is missing")
```

---

## 🌍 Mini GIS

**Safe Temperature Parser**

- Skip invalid temperature values
- Count valid values
- Calculate average temperature safely

---

## 🏆 Boss Challenge

**Robust JSON Station Loader**

- Read multiple JSON station files
- Handle missing files
- Handle missing temperature fields
- Calculate average temperature from valid stations only

---

## 📈 Progress

**Day 28 / 100 completed ✅**
