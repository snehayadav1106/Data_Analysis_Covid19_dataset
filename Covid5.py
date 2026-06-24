import  pandas as pd # for reading csv file
import matplotlib.pyplot as plt # to plot graph
import numpy as np # for array
import tkinter as tk # GUI based plotiing
from tkinter import ttk # advanced GUI of tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # braidge between matpltlib and tkinter
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "worldometer_data.csv")

df = pd.read_csv(csv_path)
df.columns=df.columns.str.strip()

cols=['Population','TotalCases','NewCases','TotalDeaths','NewDeaths','TotalRecovered','NewRecovered','ActiveCases','Serious,Critical','Tot Cases/1M pop','Deaths/1M pop','TotalTests','Tests/1M pop'] # list for filtering
root=tk.Tk() # create the GUI window
root.configure(bg='lightblue')  # Change to your desired color  # or any color name or hex code
root.title("Continent wise Data") # tttle
root.geometry("1000x600")# set the size and postion (width x height)

'''tk.Label(root,text="Select country:",pady=10).pack() #used for label only ,packed is used to display label without pack label is create but not shown
country=sorted(df["Country/Region"].unique()) # sort column in alphabetical form and remove duplicates values
combo=ttk.Combobox(root,values=country,state="readonly",width=50) # advanced combo box(selection box) which shows country region name and not allow user to Write manually only for slection
combo.set("India") # by default india selected
combo.pack(pady=5) # for showing list of 5 country'''


fig,x=plt.subplots(figsize=(10,5)) # create matplotlib and subplot of x with size below
x.set_facecolor('lightgray')  # or any color name or hex code
canvas=FigureCanvasTkAgg(fig,master=root) #convert matplotlib into tkinter GUI windo
canvas.get_tk_widget().pack(pady=20) #convert canvas into tkinter widget with 20 padding pixel
def update():
    continent = combo.get()

    # Ensure numeric conversion
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    grouped = df.groupby('Continent')[cols].sum()

    if continent not in grouped.index:
        x.clear()
        x.text(0.5, 0.5, "Continent not found", ha='center')
        canvas.draw()
        return

    values = grouped.loc[continent].fillna(0).values

    x.clear()
    bar = x.bar(cols, values, color='blue')

    for bars, val in zip(bar, values):
        x.text(bars.get_x() + bars.get_width()/2, val, str(int(val)), ha='center')

    x.set_title(f"Covid Data for {continent}")
    x.set_ylabel("Count")
    x.set_xticklabels(cols, rotation=45, ha='right')
    canvas.draw()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(root,text="Select Continent:",pady=10).pack() #used for label only ,packed is used to display label without pack label is create but not shown
continent=sorted(df["Continent"].dropna().astype(str).unique()) # sort column in alphabetical form and remove duplicates values
combo=ttk.Combobox(root,values=continent,state="readonly",width=50) # advanced combo box(selection box) which shows country region name and not allow user to Write manually only for slection
combo.set(continent[0]) # by default india selected
combo.pack(pady=5) # for showing list of 5 country




tk.Button(root, text="Update Chart", command=update,bg='Black',fg='White').pack(pady=10)

#tk.Button(root,text="filter",command=update).pack() # for button label command to trigger update function
root.mainloop() #is the final command in a Tkinter application that starts the event loop — the heart of any GUI program




