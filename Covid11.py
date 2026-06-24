import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "day_wise.csv")

df = pd.read_csv(csv_path)

df['Date']=pd.to_datetime(df['Date'],format='%d-%m-%Y')
April=df[df['Date'].dt.month==4]
cols=['Confirmed','Deaths','Recovered','Active','New cases','New deaths','New recovered']
x=April.groupby('Date')[cols].sum()

value=April[cols].sum()
plt.pie(value, labels=cols, autopct=lambda p: f'{p:.1f}%\n({int(p * value.sum() / 100)})', startangle=140)



    
   # for i,val in enumerate(x[col]):
    #    plt.text(x.index[i],val,str(val),ha='center')
plt.title("April Month covid data")
plt.legend()
plt.show()