# Day 29 - Comprehension & JSON Error Filtering

## 📚 What I Learned

Today I learned:

- List comprehension
- Dict comprehension
- Filtering with `if`
- Using `zip()` to build dictionaries
- `json.JSONDecodeError`
- Combining `try/except` with comprehensions

---

## 💻 Practice

### ✔ Add 2°C to every temperature

```python
temperatures = [28, 31, 25, 35, 20]
adjusted = [temp + 2 for temp in temperatures]
print(adjusted)
```

### ✔ Filter temperatures below 25

```python
temperatures = [28, 31, 25, 35, 20]
cold = [temp for temp in temperatures if temp < 25]
print(cold)
```

### ✔ Build a station dictionary

```python
stations = ["HY01", "HY02", "HY03"]
temps = [28, 31, 25]

station_temps = {name: temp for name, temp in zip(stations, temps)}
print(station_temps)
```

---

## 🌍 Mini GIS

**Station Classifier**

- Create dictionaries for hot stations (`temp >= 30`)
- Create dictionaries for cold stations (`temp < 25`)
- Count stations in each category

---

## 🏆 Boss Challenge

**JSON Error Filter Pipeline**

- Parse multiple JSON lines
- Skip invalid JSON records
- Skip records missing `temp`
- Build a final filtered dictionary using dict comprehension

---

## 📈 Progress

**Day 29 / 100 completed ✅**
