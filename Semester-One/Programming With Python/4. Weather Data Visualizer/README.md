# Weather Data Visualizer  

A simple Python script to clean, analyze and visualize historical weather data of Delhi  with monthly & yearly trends using temperature and rainfall data.  

<img width="1200" height="400" alt="image" src="https://github.com/user-attachments/assets/ec0d067c-dc64-47f2-a9f0-2acca5c6e625" />
<img width="1000" height="400" alt="image" src="https://github.com/user-attachments/assets/a47fd832-7135-4bc2-9a13-00c6981b9c7a" />
<p align="center">
  <img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/841e459f-64be-4229-9dab-bbdf767897e7" />
  <img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/6aed46e0-f2a0-454d-99cf-9231b12263c8" />
</p>


---

## Features  

- Cleans raw weather data: handles missing dates & temperatures, filters by date range (2010 onwards)  
- Generates key statistics: average / min / max / std. deviation for max temperatures  
- Visualizes climate trends with neat plots:  
  - Monthly-average max temperature line chart  
  - Monthly rainfall bar chart  
  - Min vs Max temperature scatter (monthly averages)  
  - Combined plots for quick overview  
- Aggregates data by month and year for long-term trend analysis  
- Exports cleaned data to CSV for further analysis / sharing  

---

## Project Structure  
```
weather-data-visualizer/
│── data.csv # Raw input dataset (rename as needed)
│── weather_visualizer.py # Main script
│── delhi_weather_cleaned.csv # Cleaned dataset output
│── daily_temp_max.png # Monthly max-temp line chart
│── monthly_rainfall.png # Monthly rainfall bar chart
│── temp_scatter.png # Monthly Min vs Max temp scatter
│── combined_plots.png # Combined summary figure
└── README.md # This file
```


---

## How to Run  

1. Clone or download the repo  
2. Place your raw weather dataset as `data.csv` (or edit file path in code)  
3. Install dependencies (if not already):  
   ```bash
   pip install pandas numpy matplotlib
4. Run the script
```bash 
   python weather_visualizer.py
```
5. Outputs will be generated automatically: cleaned CSV + plots

## Usage Example
```
$ python weather_visualizer.py  
--- Dataset Info ---  
<class 'pandas.core.frame.DataFrame'>  
RangeIndex: 4000 entries, 0 to 3999  
...  

** Temperature Statistics (Max Temp) **  
Average Max Temp: 32.7  
Minimum Max Temp: 22.5  
Maximum Max Temp: 45.2  
Std Dev Max Temp: 4.2  

Saved: delhi_weather_cleaned.csv  
Saved: daily_temp_max.png  
Saved: monthly_rainfall.png  
Saved: temp_scatter.png  
Saved: combined_plots.png  
All tasks completed successfully!
```
After running, you’ll find plots and cleaned data ready for inspection or further analysis.

## Dependencies
- Python 3.7+
- pandas
- numpy
- matploylib

## Assignment Tasks Completed

- ✅ Task 1: Data Acquisition and Loading
- ✅ Task 2: Data Cleaning and Processing
- ✅ Task 3: Statistical Analysis with NumPy
- ✅ Task 4: Task 4: Visualization with Matplotlib
- ✅ Task 5: Grouping and Aggregation
- ✅ Task 6: Export and Storytelling
---

## Author

- Prabhat Bhatia
- B.Tech CSE Cyber Security(First Semester)
- 29th November 2025
- Programming With Python - Lab Assignment 4
