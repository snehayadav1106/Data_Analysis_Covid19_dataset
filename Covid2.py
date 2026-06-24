import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkcalendar import DateEntry
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "day_wise.csv")

df = pd.read_csv(csv_path)
df.columns = df.columns.str.strip()
df['Date'] = pd.to_datetime(df['Date'])

cols = ['Confirmed','Deaths','Recovered','Active','New cases','New deaths','New recovered']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

def update():
    sdate = pd.Timestamp(start_cal.get_date())
    edate = pd.Timestamp(end_cal.get_date())
    filtered_df = df[(df['Date'] >= sdate) & (df['Date'] <= edate)]
    
    ax.clear()
    width = 0.1
    xpos = np.arange(len(filtered_df['Date']))
    
    for i, col in enumerate(cols):
        ax.bar(xpos + width*i, filtered_df[col], width=width, label=col)
    
        for j, val in enumerate(filtered_df[col]):
            ax.text(xpos[j] + width*i, val, str(int(val)), ha='center', va='bottom', fontsize=8)
    
    
    ax.set_xticks(xpos + width*len(cols)/2)
    ax.set_xticklabels(filtered_df['Date'].dt.strftime('%d-%m-%Y'), rotation=45)
    ax.set_title("COVID Data by Date")
    ax.set_ylabel("Count")
    ax.legend()
    
    canvas.draw()

root = tk.Tk()
root.title("Covid Data")
root.geometry("1200x600")

fig, ax = plt.subplots(figsize=(14,8))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Start Date:").grid(row=0, column=0, padx=5, pady=5)
start_cal = DateEntry(frame, date_pattern='dd-mm-yyyy')
start_cal.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="End Date:").grid(row=1, column=0, padx=5, pady=5)
end_cal = DateEntry(frame, date_pattern='dd-mm-yyyy')
end_cal.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Update Chart", command=update).pack(pady=10)

root.mainloop()
