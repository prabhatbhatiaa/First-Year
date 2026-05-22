# Name: Prabhat Bhatia
# Date: 29/11/2025
# Project: Weather Data Visualizer
# Assignment No: 4

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Task 1: Data Acquisition and Loading
data = pd.read_csv('C:\\Users\\Admin\\Desktop\\College\\Assignments\\Programming With Python\\Assignment 4\\data.csv')

print("\n** Dataset Info **")
print(data.info())

# Task 2: Data Cleaning and Processing
data["Date"] = pd.to_datetime(data["Date"])
data = data.dropna(subset=["Date"])

# 🔥 Filter dataset to only 2010 onwards
data = data[data["Date"].dt.year >= 2010]

data = data.rename(columns={
    "Temp Max": "temp_max",
    "Temp Min": "temp_min",
    "Rain": "rain"
})

# Add month and year columns for grouping
data["month"] = data["Date"].dt.month
data["year"] = data["Date"].dt.year

# Fill the single missing value
data["temp_min"] = data["temp_min"].fillna(data["temp_min"].mean())

# Task 3: Statistical Analysis with NumPy
avg_max = np.mean(data["temp_max"])
min_max = np.min(data["temp_max"])
max_max = np.max(data["temp_max"])
std_max = np.std(data["temp_max"])

print("\n** Temperature Statistics (Max Temp) **")
print("Average Max Temp:", avg_max)
print("Minimum Max Temp:", min_max)
print("Maximum Max Temp:", max_max)
print("Std Dev Max Temp:", std_max)

# Task 4: Visualization with Matplotlib

# 1. Line chart for monthly temperature trends (one dot per month)
monthly_temp = data.resample("M", on="Date")["temp_max"].mean()

plt.figure(figsize=(10, 4))
plt.plot(monthly_temp.index, monthly_temp.values, marker='o')
plt.title("Monthly Average Max Temperature – Delhi (2010 onwards)")
plt.xlabel("Year")
plt.ylabel("Max Temperature (°C)")
plt.savefig("daily_temp_max.png")
plt.close()

# 2. Bar chart for monthly rainfall averages
plt.figure(figsize=(8, 4))
data.groupby("month")["rain"].mean().plot(kind="bar")
plt.title("Average Monthly Rainfall – Delhi")
plt.xlabel("Month Number")
plt.ylabel("Rainfall (mm)")
plt.savefig("monthly_rainfall.png")
plt.close()

# 3. Scatter plot for monthly avg min vs max temperature (FIXED)
monthly_min = data.resample("M", on="Date")["temp_min"].mean()
monthly_max = data.resample("M", on="Date")["temp_max"].mean()

plt.figure(figsize=(6, 4))
plt.scatter(monthly_min.values, monthly_max.values)
plt.title("Monthly Avg Min vs Max Temperature")
plt.xlabel("Monthly Avg Min Temp")
plt.ylabel("Monthly Avg Max Temp")
plt.savefig("temp_scatter.png")
plt.close()

# 4. Combined Plot
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

axs[0].plot(monthly_temp.index, monthly_temp.values, marker='o')
axs[0].set_title("Monthly Avg Max Temp")

axs[1].scatter(monthly_min.values, monthly_max.values)
axs[1].set_title("Monthly Avg Min vs Max Temp")

plt.savefig("combined_plots.png")
plt.close()

# Task 5: Grouping and Aggregation

# Monthly Stats
monthly_stats = data.groupby("month")[["temp_max", "temp_min", "rain"]].mean()
print("\nMonthly Statistics:")
print(monthly_stats)

# Yearly Stats
yearly_stats = data.groupby("year")[["temp_max", "temp_min", "rain"]].mean()
print("\nYearly Statistics:")
print(yearly_stats)

# Task 6: Export and Storytelling
data.to_csv("delhi_weather_cleaned.csv", index=False)

print("\nSaved: delhi_weather_cleaned.csv")
print("Saved: daily_temp_max.png")
print("Saved: monthly_rainfall.png")
print("Saved: temp_scatter.png")
print("Saved: combined_plots.png")
print("\nAll tasks completed successfully!")
