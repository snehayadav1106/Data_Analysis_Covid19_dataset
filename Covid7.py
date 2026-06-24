import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tkcalendar import DateEntry
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "day_wise.csv")

df = pd.read_csv(csv_path)
df.columns=df.columns.str.strip()
df['Date']=pd.to_datetime(df['Date'],format='%d-%m-%Y')

cols=['Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered']
df[cols]=df[cols].apply(pd.to_numeric)

def update():
    sdate=pd.Timestamp(startd.get_date())
    filtered_df=df[df['Date']==sdate]

    x.clear()
    if not filtered_df.empty:
        values = filtered_df[cols].values.flatten()

        def format_autopct(pct):
            total = sum(values)
            val = pct * total / 100.0
            return f"{pct:.1f}%\n({val:.2f})"

        wedges, texts, autotexts = x.pie(values,labels=cols,autopct=format_autopct,colors=['red', 'green', 'blue'],startangle=90)



    canvas.draw()

root=tk.Tk()
root.title("Covid data")
root.configure(bg='Lightgreen')
root.geometry("1000x600")

fig,x=plt.subplots(figsize=(12,6))
canvas=FigureCanvasTkAgg(fig,master=root)
canvas.get_tk_widget().pack(pady=20)

frame=tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame,text="Select Date:").grid(row=0,column=0,padx=5,pady=5)
startd=DateEntry(frame,date_pattern='dd-mm-yyyy')
startd.grid(row=0,column=0,pady=5,padx=5)

tk.Button(root,text="Update",command=update,bg='green',fg='white').pack(pady=10)
root.mainloop()


