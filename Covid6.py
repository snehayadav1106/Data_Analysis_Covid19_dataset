import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "country_wise_latest.csv")

df = pd.read_csv(csv_path)
df.columns=df.columns.str.strip()

cols=['Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered']
root=tk.Tk()
root.configure(bg='pink')
root.title("Country wise data")
root.geometry("1000x600")

'''tk.Label(root,text="Select country:",pady=10).pack()
country=sorted(df['Country/Region'].unique())
combo=ttk.Combobox(root,values=country,state="readonly",width=50)
combo.set("India")
combo.pack(pady=5)'''

fig,x=plt.subplots(figsize=(10,5))
canvas=FigureCanvasTkAgg(fig,master=root)
canvas.get_tk_widget().pack(pady=20)

def update():
    country=combo.get()
    row=df[df['Country/Region']==country]

    if row.empty:
        x.clear()
        x.axis('off')
        x.text("country ot found",ha='center')
        canvas.draw()
        return
    values = [float(row[col].values[0]) for col in cols]
    x.clear()
    def format_autopct(pct):
        total = sum(values)
        val = pct * total / 100.0
        return f"{pct:.1f}%\n({val:.2f})"

    wedges, texts, autotexts = x.pie(
        values,
        labels=cols,
        autopct=format_autopct,
        colors=['red', 'green', 'blue']
    )

    canvas.draw()


frame=tk.Frame(root)
frame.pack(pady=10)

tk.Label(root,text="Select country:",pady=10,bg='Pink').pack()
country=sorted(df['Country/Region'].unique())
combo=ttk.Combobox(root,values=country,state="readonly",width=50)
combo.set("India")
combo.pack(pady=5)

tk.Button(root,text="Filter",command=update,bg='purple',fg='white').pack(pady=10)
root.mainloop()