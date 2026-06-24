import matplotlib.pyplot as plt
import pandas as pd

import os


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "day_wise.csv")

df = pd.read_csv(csv_path)

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

June= df[(df['Date'].dt.month == 6) & (df['Date'].dt.year == 2020)]

cols = ['Confirmed', 'Deaths', 'Recovered', 'Active', 'New cases', 'New deaths', 'New recovered']
totals = June[cols].sum()

plt.figure(figsize=(12, 6))
x = range(len(cols))
y = totals.values

plt.scatter(x, y, color='skyblue', edgecolors='black', s=100)

for i, value in enumerate(y):
    plt.text(x[i], value, f'{int(value):,}', ha='center', va='bottom', fontsize=10)

plt.xticks(x, cols)
plt.title("Total COVID-19 Metrics for June 2020")
plt.xlabel("Metrics")
plt.ylabel("Total Count")

plt.show()