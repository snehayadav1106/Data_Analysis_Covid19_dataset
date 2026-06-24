import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "country_wise_latest.csv")

df = pd.read_csv(csv_path)
df.columns = df.columns.str.strip()
top10 = df.nlargest(10,'Recovered')
plt.subplot(2,1,1)
plt.bar(top10['Country/Region'], top10['Recovered'],color='pink')
for index, value in enumerate(top10['Recovered']):
    plt.text(index, value + 1000, str(value), ha='center', va='bottom', fontsize=9)

plt.ylabel('Recovered Cases')
plt.title('Top 10 Countries by  largest recovered COVID-19 Cases')
#plot 2

lowest10 = df.nsmallest(10,'Recovered')
plt.subplot(2,1,2)
plt.bar(lowest10['Country/Region'], lowest10['Recovered'],color='pink')
for index, value in enumerate(lowest10['Recovered']):
    plt.text(index, value , str(value), ha='center', va='bottom', fontsize=9)
plt.xlabel('Country/Region')
plt.ylabel('Recovered Cases')
plt.title('Top 10 Countries by smallest recovered COVID-19 Cases')
plt.show()


