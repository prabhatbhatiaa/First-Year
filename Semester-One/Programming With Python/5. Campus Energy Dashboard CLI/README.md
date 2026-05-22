# Campus Energy-Use Dashboard

A simple, beginner-friendly Python project that ingests building meter CSVs, cleans and enriches the data, computes daily / weekly / building-level aggregates, and produces a compact dashboard + executive summary for a campus. Designed to be clear, viva-safe, and easy to run.

<img width="2000" height="600" alt="image" src="https://github.com/user-attachments/assets/406e316c-69e5-419b-8e00-ec314de536c7" />

---

## Features
- Reads multiple building CSV files from `data/` (auto-detects `.csv` files).
- Cleans timestamps and standardizes columns (`building_name`, `timestamp`, `month`, `kwh`).
- Adds `month` column for monthly aggregations.
- Computes daily and weekly totals using `resample`.
- Building-wise statistics: total, mean, min, max.
- Simple object model (MeterReading, Building, BuildingManager) for building-level analysis.
- Produces a 3-panel dashboard (`dashboard.png`):  
  - daily usage trend  
  - weekly average usage per building  
  - daily peak usage scatter
- Exports a cleaned CSV, a building summary CSV, and a readable `summary.txt` executive report.

---

## Project Structure
```text
campus-energy-dashboard/
│── data/
│     ├── A_block.csv
│     ├── B_block.csv
│     ├── C_block.csv
│     └── D_block.csv
│── output/
│     ├── cleaned_energy_data.csv
│     ├── building_summary.csv
│     ├── summary.txt
│     └── dashboard.png
│── main.py
└── README.md
```
---

## Expected CSV Format 

Each CSV should ideally follow this structure:
```
building_name,timestamp,month,kwh
A_block,2024-01-01 00:00:00,1,32.4
```
If a file is missing building_name, the filename is used.
If time is present instead of timestamp, it is auto-corrected.
If usage appears instead of kwh, it is auto-renamed.

---
## How to Run  
1. Put all building CSVs into the data/ folder.
2. Ensure output/ folder exists.
3. Install dependencies:
```bash
pip install pandas numpy matplotlib
```
4. Run the script:
```bash
python main.py
```
5. After running, check the output/ folder for:
- cleaned_energy_data.csv
- building_summary.csv
- dashboard.png
- summary.txt

---

## Console Output
```
No. of CSV files read: 4
Combined rows: 120
Daily totals computed: 10 days
Saved: output/cleaned_energy_data.csv
Saved: output/building_summary.csv
Saved: output/dashboard.png
Saved: output/summary.txt
Capstone project executed successfully. Check output folder for results.
```

## Summary
```
--= Campus Total Energy Usage =--

Total Energy Usage across Campus: 4039.0000000000005 kWh
Highest Consuming Building: C_block : 1318.3 kWh
--= Building-wise Summary =--

-> Building: A_block
-> Total Readings: 30
-> Total Energy Usage: 1074.5 kWh
-> Average Energy Usage: 35.81666666666667 kWh
-> Min Energy Usage: 27.6 kWh
-> Max Energy Usage: 47.4 kWh

-> Building: D_block
-> Total Readings: 30
-> Total Energy Usage: 918.9 kWh
-> Average Energy Usage: 30.63 kWh
-> Min Energy Usage: 23.8 kWh
-> Max Energy Usage: 39.4 kWh

-> Building: C_block
-> Total Readings: 30
-> Total Energy Usage: 1318.3 kWh
-> Average Energy Usage: 43.943333333333335 kWh
-> Min Energy Usage: 35.9 kWh
-> Max Energy Usage: 53.6 kWh

-> Building: B_block
-> Total Readings: 30
-> Total Energy Usage: 727.3 kWh
-> Average Energy Usage: 24.243333333333332 kWh
-> Min Energy Usage: 18.8 kWh
-> Max Energy Usage: 30.2 kWh

--= Peak Usages per Building =--

Building: A_block | Peak Usage: 47.4 kWh at 2024-01-08 16:00:00
Building: D_block | Peak Usage: 39.4 kWh at 2024-01-10 16:00:00
Building: C_block | Peak Usage: 53.6 kWh at 2024-01-09 16:00:00
Building: B_block | Peak Usage: 30.2 kWh at 2024-01-07 16:00:00
```
---
## Dependencies
- Python 3.8+
- pandas
- numpy
- matploylib

## Assignment Tasks Completed

- ✅ Task 1 — Data Ingestion & Validation
- ✅ Task 2 — Aggregation Logic
- ✅ Task 3 — Object-Oriented Modeling
- ✅ Task 4 — Visualization Dashboard
- ✅ Task 5 — Persistence + Executive Summary
---

## Troubleshooting

- If it says “No valid CSV file found”, make sure files are inside ```data/``` and end with .csv.
- If timestamp parsing fails, ensure the timestamp format is ```YYYY-MM-DD HH:MM:SS```.
- If dashboard looks compressed, open dashboard.png directly
---

## Author
- Prabhat Bhatia
- B.Tech CSE Cyber Security(First Semester)
- 3rd December 2025
- Programming With Python - Lab Assignment 5(Capstone)
