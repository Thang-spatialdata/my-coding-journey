Day 26 - File Read & Write

📚 What I Learned

Today I learned:

- "open()"
- Writing files with ""w""
- Reading files with "read()"
- Reading lines with "readlines()"
- Cleaning text with ".strip()"
- Splitting CSV-style data with ".split(",")"
- Appending new data with ""a"" mode

I also practiced processing GIS-style station data stored in text files.

---

💻 Practice

✔ Write station records to "stations.txt"

✔ Read and print clean lines

✔ Parse station name and temperature

✔ Display formatted station reports

---

🌍 Mini GIS

Built a Station Log Writer that:

- Writes station data from a dictionary into "station_log.txt"
- Reads the file again without using the original dictionary
- Extracts temperatures from the file
- Calculates the average temperature from the stored data
- Prints the average temperature report

---

🏆 Boss Challenge

Built a Raw Data Cleaner that:

- Writes messy raw station data into "raw_data.txt"
- Removes extra spaces
- Removes duplicate records
- Removes invalid rows with missing temperature values
- Converts station names to uppercase
- Saves cleaned data into "clean_data.txt"
- Prints the number of removed and remaining records

---

🚀 Python Journey — Day 26/100
