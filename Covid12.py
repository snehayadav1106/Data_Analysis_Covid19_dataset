import matplotlib.pyplot as plt
import pandas as pd


import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "day_wise.csv")

df = pd.read_csv(csv_path)
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
may = df[(df['Date'].dt.month == 5) & (df['Date'].dt.year == 2020)]
cols = ['Confirmed', 'Deaths', 'Recovered', 'Active', 'New cases', 'New deaths', 'New recovered']
totals = may[cols].sum()
plt.figure(figsize=(12, 6))
bars = plt.bar(cols, totals, color='skyblue', edgecolor='black')


for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{int(height):,}', ha='center', va='bottom', fontsize=10)


plt.title("Total COVID-19 Metrics for May 2020")
plt.xlabel("Metrics")
plt.ylabel("Total Count")

plt.show()