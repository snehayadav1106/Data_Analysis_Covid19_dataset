import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

import os


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "day_wise.csv")

df = pd.read_csv(csv_path)
# simple plot with marker
df['Date']=pd.to_datetime(df['Date'],format='%d-%m-%Y')
january=df[df['Date'].dt.month==1]
cols=['Confirmed','Deaths','Recovered','Active','New cases','New deaths','New recovered']
x=january.groupby('Date')[cols].sum()
for col in cols:
    plt.plot(x[col],label=col)
    for i,val in enumerate(x[col]):
        plt.text(x.index[i],val,str(val),ha='center')
plt.xlabel("January Dates")
plt.ylabel("Total count")
plt.title("January Month covid data")
plt.legend()
plt.grid()
plt.show()