import  pandas as pd # for reading csv file
import matplotlib.pyplot as plt # to plot graph
import numpy as np # for array
import tkinter as tk # GUI based plotiing
from tkinter import ttk # advanced GUI of tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # braidge between matpltlib and tkinter
import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "country_wise_latest.csv")

df = pd.read_csv(csv_path)
df.columns=df.columns.str.strip()

cols=['Confirmed','Deaths','Recovered','Active','New cases','New deaths','New recovered'] # list for filtering
root=tk.Tk() # create the GUI window
root.title("Country wise Data") # tttle
root.geometry("1000x600")# set the size and postion (width x height)




fig,x=plt.subplots(figsize=(10,5)) # create matplotlib and subplot of x with size below
canvas=FigureCanvasTkAgg(fig,master=root) #convert matplotlib into tkinter GUI windo
canvas.get_tk_widget().pack(pady=20) #convert canvas into tkinter widget with 20 padding pixel

def update(): # function to update graph
    country=combo.get() # method use to get tkinter selected value from combo box
    row=df[df['Country/Region']==country] # df for only country.region matches the selected country


    if row.empty: #if not selected or country not found in data
        x.clear() # clear the previous graph
        x.text(0.5,0.5,"country not found",ha='center')
        canvas.draw() # updates the embedded graph
        return # execution stop for errors and unecesssary ploting
    values=[row[col].values[0] for col in cols] #create new row col fetches country name from cols and print 1st index that is 'confirmed'
    x.clear() # clear the plot
    bar=x.bar(cols,values,color='red') # plot new bar

    for bars,val in zip(bar,values): # to show exact value on bar
        x.text(bars.get_x() + bars.get_width()/2, val, str(int(val)), ha='center') # postion for values
    x.set_title("Coivid data") # used for label and titles
    x.set_ylabel("count")
    x.set_xlabel(cols)
    canvas.draw()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(root,text="Select country:",pady=10).pack() #used for label only ,packed is used to display label without pack label is create but not shown
country=sorted(df["Country/Region"].unique()) # sort column in alphabetical form and remove duplicates values
combo=ttk.Combobox(root,values=country,state="readonly",width=50) # advanced combo box(selection box) which shows country region name and not allow user to Write manually only for slection
combo.set("India") # by default india selected
combo.pack(pady=5) # for showing list of 5 country




tk.Button(root, text="Update Chart", command=update).pack(pady=10)

#tk.Button(root,text="filter",command=update).pack() # for button label command to trigger update function
root.mainloop() #is the final command in a Tkinter application that starts the event loop — the heart of any GUI program




