raw_lines = [
    "HY01, 28",
    "HY02,31",
    "HY01, 28",
    "hy03,25",
    "HY04, ",
    "HY02,31"
]

# Write raw data to file
with open("raw_lines.txt", "w") as f:
    for line in raw_lines:
        f.write(line + "\n")

tram_da_gap = set()
danh_sach_rong = []

# Read and clean data
with open("raw_lines.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")

        name = parts[0].strip().upper()
        temp = parts[1].strip()

        # Skip missing temperature
        if temp == "":
            continue

        # Skip duplicate station
        if name in tram_da_gap:
            continue

        tram_da_gap.add(name)
        danh_sach_rong.append(f"{name},{temp}")

# Write cleaned data to a new file
with open("clean_data.txt", "w") as f:
    for item in danh_sach_rong:
        f.write(item + "\n")

# Report
original_lines = len(raw_lines)
remaining_lines = len(danh_sach_rong)
removed_lines = original_lines - remaining_lines

print("=== RAW DATA CLEANER REPORT ===")
print(f"Removed lines: {removed_lines}")
print(f"Remaining lines: {remaining_lines}")
print("\nClean data:")

for item in danh_sach_rong:
    print(item)
