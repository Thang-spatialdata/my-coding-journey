# Practice 1 - Write File
with open("stations.txt", "w") as f:
    f.write("HY01,28\n")
    f.write("HY02,31\n")
    f.write("HY03,25\n")


# Practice 2 - Read Clean Lines
with open("stations.txt", "r") as f:
    for line in f.readlines():
        print(line.strip())


# Practice 3 - Parse CSV Data
with open("stations.txt", "r") as f:
    for line in f.readlines():
        clean = line.strip()
        name, temp = clean.split(",")
        print(f"Station {name}: {int(temp)}°C")
