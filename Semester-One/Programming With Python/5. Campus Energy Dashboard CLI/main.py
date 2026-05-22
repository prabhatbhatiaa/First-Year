# main.py
# Name: Prabhat Bhatia
# Capstone: Campus Energy-Use Dashboard
# Date: 2/12/25

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Task 1: Data Ingestion and Validation

data_fol = 'campus-energy-dashboard-prabhatbhatia\\data\\'
output_fol = 'campus-energy-dashboard-prabhatbhatia\\output\\'

load_fol = os.listdir(data_fol)
dataframes = []
failed_files = []

for f in load_fol:
    if f.endswith('.csv'):
        file_path = os.path.join(data_fol, f)
        try:
            df = pd.read_csv(file_path, on_bad_lines='skip')
            # Fix building_name
            if "building_name" not in df.columns:
                building_name = f.replace(".csv", "")
                df["building_name"] = building_name
            # Fix timestamp column
            if "timestamp" not in df.columns:
                if "time" in df.columns:
                    df = df.rename(columns={"time": "timestamp"})
            # Clean timestamp
            df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
            df = df.dropna(subset=["timestamp"])
            # Fix kwh column
            if "kwh" not in df.columns:
                if "usage" in df.columns:
                    df = df.rename(columns={"usage": "kwh"})
            # Add month column
            df["month"] = df["timestamp"].dt.month
            # Keep required columns
            df = df[["building_name", "timestamp", "month", "kwh"]]
            dataframes.append(df)

        except Exception as e:
            failed_files.append(f)

if len(dataframes) == 0:
    print("No valid CSV file found. PROGRAM END")
    exit()

final_data = pd.concat(dataframes, ignore_index=True)
final_data = final_data.sort_values("timestamp")

# Task 2: Core Aggregation Logic
def calculate_daily_totals(df):                 # total energy usage per day
    temp = df.set_index("timestamp")
    daily = temp["kwh"].resample("D").sum()
    return daily # not ai doing myself

def calculate_weekly_totals(df):                # total energy usage per week
    temp = df.set_index("timestamp")
    weekly = temp["kwh"].resample("W").sum()
    return weekly

def building_wise_summary(df):                  # return mean min max total kwh ie energy usage for each building
    grp = df.groupby("building_name")["kwh"]
    summary = grp.agg(['sum', 'mean', 'max', 'min']).reset_index()
    return summary

# Task 3: Object-Oriented Modeling

class Building:
    def __init__(self, name):
        self.name = name
        self.readings = []   # stores MeterReading objects

    def add_reading(self, reading):
        self.readings.append(reading)

    def total_usage(self):
        total = 0
        for r in self.readings:
            total += r.val        # FIXED
        return total

    def peak_usage(self):
        if len(self.readings) == 0:
            return None

        peak = self.readings[0]
        for r in self.readings:
            if r.val > peak.val:   # FIXED
                peak = r

        return peak.ts, peak.val    # FIXED: return timestamp + value

    def building_summary(self):
        vals = []
        for r in self.readings:
            vals.append(r.val)     # FIXED

        if len(vals) == 0:
            return {"name": self.name, "count": 0, "sum": 0, "mean": 0, "min": 0, "max": 0}

        total = sum(vals)

        return {
            "name": self.name,
            "count": len(vals),
            "sum": total,
            "mean": total / len(vals),
            "min": min(vals),
            "max": max(vals)
        }


class MeterReading:
    def __init__(self, ts, val):
        # safer timestamp parsing
        if isinstance(ts, str):
            try:
                ts = datetime.fromisoformat(ts)
            except:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
        self.ts = ts
        self.val = float(val)


class BuildingManager:
    def __init__(self):
        self.buildings = {}   # {"admin": Building(), ...}

    def load_data(self, df):
        for i in range(len(df)):
            row = df.iloc[i]
            b_name = row["building_name"]
            ts = row["timestamp"]
            val = row["kwh"]

            if b_name not in self.buildings:
                self.buildings[b_name] = Building(b_name)

            reading = MeterReading(ts, val)
            self.buildings[b_name].add_reading(reading)

    def total_campus_usage(self):
        total = 0
        for b in self.buildings.values():
            total += b.total_usage()
        return total

    def all_building_summaries(self):
        out = []
        for b in self.buildings.values():
            out.append(b.building_summary())
        return out

    def all_peak_usages(self):
        peaks = {}
        for b_name, b in self.buildings.items():
            peaks[b_name] = b.peak_usage()   # returns (ts, value)
        return peaks


manager = BuildingManager()
manager.load_data(final_data)

# Task 4: Visual Output with Matplotlib

# fetch data using our functions
daily_tot = calculate_daily_totals(final_data)
weekly_tot = calculate_weekly_totals(final_data)
building_summary = building_wise_summary(final_data)

fig, axs = plt.subplots(1,3,figsize=(20,6))

# 1. Daily usage Trend line
axs[0].plot(daily_tot.index, daily_tot.values, marker='o', linewidth=2)
axs[0].set_title('Daily Energy Usage')
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Total kWh')
axs[0].tick_params(axis='x', rotation=45)
axs[0].grid(True, linestyle='--', alpha=0.4)

# 2. Weekly usage Bar Chart
building_names = building_summary['building_name'].tolist()
weekly_avg = []
for i in building_names:
    temp = final_data[final_data['building_name'] == i]
    temp = temp.set_index('timestamp')["kwh"].resample("W").sum()
    weekly_avg.append(temp.mean())

short_labels = [x.replace("_block","") for x in building_names]

axs[1].bar(short_labels, weekly_avg, color='orange')
axs[1].set_title('Average weekly energy usage per Building')
axs[1].set_xlabel('Building')
axs[1].set_ylabel('Average kWh')
axs[1].grid(True, axis='y', linestyle='--', alpha=0.4)

# 3. Peak Usage Scatter Plot
peak_df = final_data.groupby(final_data['timestamp'].dt.date)['kwh'].max().reset_index()
peak_df.rename(columns={'timestamp':'date'}, inplace=True)

axs[2].scatter(peak_df['date'], peak_df['kwh'], color='green', s=60)
axs[2].set_title('Peak Energy Usage Over Time')
axs[2].set_xlabel('Date')
axs[2].set_ylabel('Peak kWh')
axs[2].tick_params(axis='x', rotation=45)
axs[2].grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.savefig(os.path.join(output_fol,'dashboard.png'))
plt.close()

#  Task 5: Persistence and Executive Summary

final_data.to_csv(os.path.join(output_fol,'cleaned_energy_data.csv'), index=False) # saving cleaned dataset
building_summary.to_csv(os.path.join(output_fol,'building_summary.csv'), index=False) # saving building summary

# Generating summary using task 3
campus_total = manager.total_campus_usage()
building_summaries = manager.all_building_summaries()
peak_usages = manager.all_peak_usages()

top_building = None
top_val = 0
for i in building_summaries:
    if i['sum'] > top_val:
        top_val = i['sum']
        top_building = i['name']

# summary .txt
summary_path = os.path.join(output_fol,'summary.txt')
with open(summary_path, 'w') as f:
    f.write(f"--= Campus Total Energy Usage =--\n\n")
    f.write(f"Total Energy Usage across Campus: {campus_total} kWh\n")
    f.write(f"Highest Consuming Building: {top_building} : {top_val} kWh\n")
    f.write(f"--= Building-wise Summary =--\n\n")
    for j in building_summaries:
        f.write(f"-> Building: {j['name']}\n")
        f.write(f"-> Total Readings: {j['count']}\n")
        f.write(f"-> Total Energy Usage: {j['sum']} kWh\n")
        f.write(f"-> Average Energy Usage: {j['mean']} kWh\n")
        f.write(f"-> Min Energy Usage: {j['min']} kWh\n")
        f.write(f"-> Max Energy Usage: {j['max']} kWh\n\n")

    f.write(f"--= Peak Usages per Building =--\n\n")
    for name, peak in peak_usages.items():
        if peak is not None:
            f.write(f"Building: {name} | Peak Usage: {peak[1]} kWh at {peak[0]}\n")
        else:
            f.write(f"Building: {name} | No readings available\n")


print("Capstone project executed successfully. Check output folder for results.")
