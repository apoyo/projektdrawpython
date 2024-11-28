import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from dot_plot import * 
from bar_chart import *
from pie_chart import *
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from see_graphs import *
import os 
slices = {}
colors = {}
activities = {}
frame_quantity = {}
button_choose_color={}
def create_graph(entry_title,n,username):
  
    slices_list = []
    activities_list = []
    color_list=[]
    explode_list=[]
    
    for x in range (n.get()):
        slices_list.append(int(slices[x].get()))
        activities_list.append(activities[x].get())
        color_list.append(colors[x])
        explode_list.append('0')
    path_of_file = os.getcwd()+ '\\' + username
   
    plt.rcParams["savefig.directory"] = path_of_file
    
   
    plt.pie(slices_list,labels=activities_list, colors=color_list,startangle=90, shadow = True,
        radius = 1.2, autopct = '%1.1f%%')
    
    plt.legend()
    filename = path_of_file + '\\' + entry_title.get() + '.png'
    plt.savefig(filename)
    plt.show()
def entryquantity(event_or_value,n,frame4):
    

    for widget in frame4.winfo_children():
       widget.destroy()
    for x in range(n.get()):           
        print(x)
        frame_quantity[x]=tk.Frame(frame4,width=20)
        slices[x]= tk.Entry(frame_quantity[x],width=2)
        activities[x]=tk.Entry(frame_quantity[x],width=7)
        activities[x]=tk.Entry(frame_quantity[x],width=7)
        button_choose_color[x] = tk.Button(frame_quantity[x],width=2,background='#FFF000',command=lambda x=x:choose_color(x))
        
        def choose_color(x):
            colors[x] = colorchooser.askcolor()[1]
            button_choose_color[x].config(bg=colors[x])
            print(colors)
        slices[x].pack(side=tk.LEFT)
        button_choose_color[x].pack(side=tk.RIGHT)
        activities[x].pack(side=tk.RIGHT)
    
        frame4.pack()
        frame_quantity[x].pack()

def pie_chart(frejm,username):
 
    for widget in frejm.winfo_children():
        widget.destroy()
    frejm.pack()
    title=tk.Label(frejm,text="Wpisz Tytuł")
    title.pack()
    entry_title = tk.Entry(frejm)
    entry_title.pack()
    n=tk.IntVar()
    entry_quantity_label = tk.Label(frejm,text="Liczba przycisków")
    entry_quantity_label.pack()
    label_x_y=tk.Label(frejm,width=15,text="Slices Activities")
    
    
    entry_quantity=ttk.Combobox(frejm,width=5, textvariable = n )
    entry_quantity['values'] = (1,2,3,4,5,6,7,8,9,10)
    entry_quantity['state'] = 'readonly'
    entry_quantity.pack()
    label_x_y.pack(side=tk.TOP, padx=(0, 15))
    entry_quantity.current(2)

    frame4 = tk.Frame(frejm)
    entryquantity(None,n,frame4)
    entry_quantity.bind('<<ComboboxSelected>>',lambda event: entryquantity(event, n,frame4)) 
    create_graph_button = tk.Button(frejm,text="Utwórz Wykres",command=lambda: create_graph(entry_title,n,username))
    see_graphs_button=tk.Button(frejm, text="Zobacz swoje wykresy",command=lambda: see_graphs(username))
    see_graphs_button.pack()
    create_graph_button.pack()
    



