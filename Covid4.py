import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "worldometer_data.csv")

df = pd.read_csv(csv_path)
df.columns=df.columns.str.strip()

cols=['Population']
#cols1=['TotalCases']
#cols2=['TotalDeaths']
root=tk.Tk()
root.configure(bg='lightyellow')
root.title("country wise data")
root.geometry("1000x600")


'''tk.Label(root,text="select country:",pady=10).pack()
country=sorted(df["Country/Region"].unique())
combo=ttk.Combobox(root,values=country,state="readonly",width=50)
combo.set("India")
combo.pack(pady=5)'''

fig,x=plt.subplots(figsize=(3,6))
x.set_facecolor('lightgreen') 
canvas=FigureCanvasTkAgg(fig,master=root)
canvas.get_tk_widget().pack(pady=20)

def population():
    country=combo.get()
    row=df[df['Country/Region']==country]
    x.clear()

    if row.empty:
        x.clear()
        x.text(0.5,0.5,"Country not found",ha='center')
        canvas.draw()
        return
    cols = ['Population']
    values = [row[col].values[0] for col in cols]
    bar = x.bar(cols, values, color='Green',width=0.1)

    for bars, val in zip(bar,values):
        x.text(bars.get_x() + bars.get_width()/2,val,str(int(val)),ha='center')
    x.set_title("Covid data")
    x.set_ylabel("Count")
    x.set_xlabel(cols)
    canvas.draw()
def clear_plot(event=None):
    x.clear()
    x.text(0.5, 0.5, "Select a Button", ha='center')
    x.set_title("Covid data")
    canvas.draw()

frame=tk.Frame(root)
frame.pack(pady=10)

tk.Label(root,text="Select country",pady=10).pack()
country=sorted(df["Country/Region"].unique())
combo=ttk.Combobox(root,values=country,state="readonly",width=50)
combo.set("India")
combo.pack(pady=5)

combo.bind("<<ComboboxSelected>>", clear_plot)


tk.Button(root,text="POPULATION",command=population,bg='Green',fg='White').pack(padx=20,side='left')

# for total cases

def totalcase():
    country=combo.get()
    row=df[df['Country/Region']==country]
    x.clear()

    if row.empty:
        x.clear()
        x.text(0.5,0.5,"Country not found",ha='center')
        canvas.draw()
        return
    cols = ['TotalCases']
    values = [row[col].values[0] for col in cols]
    bar = x.bar(cols, values, color='Blue',width=0.1)

    for bars, val in zip(bar,values):
        x.text(bars.get_x() + bars.get_width()/2,val,str(int(val)),ha='center')
    x.set_title("Covid data")
    x.set_ylabel("Count")
    x.set_xlabel(cols)
    canvas.draw()

tk.Button(root,text="Total Cases",command=totalcase,bg='Blue',fg='White').pack(side='left',padx=20)

# for total deaths
def totaldeaths():
    country=combo.get()
    row=df[df['Country/Region']==country]
    x.clear()

    if row.empty:
        x.clear()
        x.text(0.5,0.5,"Country not found",ha='center')
        canvas.draw()
        return
    cols = ['TotalDeaths']
    values = [row[col].values[0] for col in cols]
    bar = x.bar(cols, values, color='black',width=0.1)

    for bars, val in zip(bar,values):
        x.text(bars.get_x() + bars.get_width()/2,val,str(int(val)),ha='center')
    x.set_title("Covid data")
    x.set_ylabel("Count")
    x.set_xlabel(cols)
    canvas.draw()
tk.Button(root,text="TotalDeaths",command=totaldeaths,bg='black',fg='White').pack(padx=20,side='left')

# total recovered
def totalrecovered():
    country=combo.get()
    row=df[df['Country/Region']==country]
    x.clear()

    if row.empty:
        x.clear()
        x.text(0.5,0.5,"Country not found",ha='center')
        canvas.draw()
        return
    cols = ['TotalRecovered']
    values = [row[col].values[0] for col in cols]
    bar = x.bar(cols, values, color='yellow',width=0.1)

    for bars, val in zip(bar,values):
        x.text(bars.get_x() + bars.get_width()/2,val,str(int(val)),ha='center')
    x.set_title("Covid data")
    x.set_ylabel("Count")
    x.set_xlabel(cols)
    canvas.draw()
tk.Button(root,text="Total Recovered",command=totalrecovered,bg='yellow',fg='black').pack(padx=20,side='left')


# Active casesdef acivecases():
country=combo.get()
row=df[df['Country/Region']==country]
x.clear()

if row.empty:
    x.clear()
    x.text(0.5,0.5,"Country not found",ha='center')
    canvas.draw()
    
cols = ['ActiveCases']
values = [row[col].values[0] for col in cols]
bar = x.bar(cols, values, color='purple',width=0.1)

for bars, val in zip(bar,values):
    x.text(bars.get_x() + bars.get_width()/2,val,str(int(val)),ha='center')
    x.set_title("Covid data")
    x.set_ylabel("Count")
    x.set_xlabel(cols)
    canvas.draw()
tk.Button(root,text="Active Cases",command="AciveCases",bg='Purple',fg='white').pack(padx=20,side='left')

# Serious,Critical
def serious():
    country=combo.get()
    row=df[df['Country/Region']==country]
    x.clear()

    if row.empty:
        x.clear()
        x.text(0.5,0.5,"Country not found",ha='center')
        canvas.draw()
        return
    cols = ['Serious,Critical']
    values = [row[col].values[0] for col in cols]
    bar = x.bar(cols, values, color='grey',width=0.1)

    for bars, val in zip(bar,values):
        x.text(bars.get_x() + bars.get_width()/2,val,str(int(val)),ha='center')
    x.set_title("Covid data")
    x.set_ylabel("Count")
    x.set_xlabel(cols)
    canvas.draw()

tk.Button(root,text="Serious, Citical",command=serious,bg='grey',fg='black').pack(padx=20,side='left')

# total cases /1M people
def tot_pop():
    country=combo.get()
    row=df[df['Country/Region']==country]
    x.clear()

    if row.empty:
        x.clear()
        x.text(0.5,0.5,"Country not found",ha='center')
        canvas.draw()
        return
    cols = ['Tot Cases/1M pop']
    values = [row[col].values[0] for col in cols]
    bar = x.bar(cols, values, color='orange',width=0.1)

    for bars, val in zip(bar,values):
        x.text(bars.get_x() + bars.get_width()/2,val,str(int(val)),ha='center')
    x.set_title("Covid data")
    x.set_ylabel("Count")
    x.set_xlabel(cols)
    canvas.draw()

tk.Button(root,text="Tot Cases/1M pop",command=tot_pop,bg='orange',fg='black').pack(padx=20,side='left')

# tot dealts 1M people

def tot_death():
    country=combo.get()
    row=df[df['Country/Region']==country]
    x.clear()

    if row.empty:
        x.clear()
        x.text(0.5,0.5,"Country not found",ha='center')
        canvas.draw()
        return
    cols = ['Deaths/1M pop']
    values = [row[col].values[0] for col in cols]
    bar = x.bar(cols, values, color='brown',width=0.1)

    for bars, val in zip(bar,values):
        x.text(bars.get_x() + bars.get_width()/2,val,str(int(val)),ha='center')
    x.set_title("Covid data")
    x.set_ylabel("Count")
    x.set_xlabel(cols)
    canvas.draw()

tk.Button(root,text="Deaths/1M pop",command=tot_death,bg='brown',fg='white').pack(padx=20,side='left')

#total test
def tot_test():
    country=combo.get()
    row=df[df['Country/Region']==country]
    x.clear()

    if row.empty:
        x.clear()
        x.text(0.5,0.5,"Country not found",ha='center')
        canvas.draw()
        return
    cols = ['TotalTests']
    values = [row[col].values[0] for col in cols]
    bar = x.bar(cols, values, color='pink',width=0.1)

    for bars, val in zip(bar,values):
        x.text(bars.get_x() + bars.get_width()/2,val,str(int(val)),ha='center')
    x.set_title("Covid data")
    x.set_ylabel("Count")
    x.set_xlabel(cols)
    canvas.draw()

tk.Button(root,text="TotalTests",command=tot_test,bg='pink',fg='black').pack(padx=20,side='left')
# tests/1M pop
def test_pop():
    country=combo.get()
    row=df[df['Country/Region']==country]
    x.clear()

    if row.empty:
        x.clear()
        x.text(0.5,0.5,"Country not found",ha='center')
        canvas.draw()
        return
    cols = ['Tests/1M pop']
    values = [row[col].values[0] for col in cols]
    bar = x.bar(cols, values, color='red',width=0.1)

    for bars, val in zip(bar,values):
        x.text(bars.get_x() + bars.get_width()/2,val,str(int(val)),ha='center')
    x.set_title("Covid data")
    x.set_ylabel("Count")
    x.set_xlabel(cols)
    canvas.draw()

tk.Button(root,text="Tests/1M pop",command=test_pop,bg='red',fg='black').pack(padx=20,side='left')


root.mainloop()



