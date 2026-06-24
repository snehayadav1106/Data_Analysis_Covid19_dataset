import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

import os


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "day_wise.csv")

df = pd.read_csv(csv_path)
df.columns=df.columns.str.strip()

df['Date']=pd.to_datetime(df['Date'],format='%d-%m-%Y')
df['Month']=df['Date'].dt.strftime('%B')
data=df[df['Date'].dt.month.isin([1,2,3,4,5,6,7])]
month=['January','Febuary','March','April','May','June','July']
cols=['Confirmed','Deaths','Recovered','Active','New cases','New deaths','New recovered']
x=data.groupby('Month')[cols].sum().reset_index()
x['Month']=pd.Categorical(x['Month'], categories=month,ordered=True)
plot=x.melt(id_vars='Month',value_vars=cols,value_name='Count',var_name='Metric')
plott=sns.barplot(data=plot, x='Month', y='Count', hue='Metric')
for container in plott.containers:
    plott.bar_label(container, fmt='%.0f', label_type='edge')



plt.suptitle("total cases month wise")
plt.show()

