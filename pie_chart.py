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
slices = {}
colors = {}
activities = {}
frame_quantity = {}
def create_graph(entry_title,n):
    #print(name_axis_x.get())
    #print("Drukuje dlugosc tablicy")
    slices_list = []
    activities_list = []
    color_list=[]
    explode_list=[]
    for x in range (n.get()):
        slices_list.append(int(slices[x].get()))
        activities_list.append(activities[x].get())
        color_list.append(colors[x])
        explode_list.append('0')

   
    plt.pie(slices_list,labels=activities_list, colors=color_list,startangle=90, shadow = True,
        radius = 1.2, autopct = '%1.1f%%')
    
    plt.legend()
    plt.show()
def entryquantity(event_or_value,n,frame4):
    print('Klantity dziala')

    for widget in frame4.winfo_children():
       widget.destroy()
    for x in range(n.get()):           
        print(x)
        frame_quantity[x]=tk.Frame(frame4)
        slices[x]= tk.Entry(frame_quantity[x],width=2)
        activities[x]=tk.Entry(frame_quantity[x],width=7)
        activities[x]=tk.Entry(frame_quantity[x],width=7)
        label_x_y=tk.Label(frame_quantity[x],width=2,text="Slices and activities")
        label_x_y.pack(side=tk.TOP)
        slices[x].pack(side=tk.LEFT)
        activities[x].pack(side=tk.RIGHT)
        button_choose_color = tk.Button(frame_quantity[x],width=5,text="Choose color",command=lambda x=x:choose_color(x))
        button_choose_color.pack()
        def choose_color(x):
            colors[x] = colorchooser.askcolor()[1]
            print(colors)
        frame4.pack()
        frame_quantity[x].pack()

def pie_chart(frejm):
    print('Wykres kołowy')
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
    
    entry_quantity=ttk.Combobox(frejm,width=5, textvariable = n )
    entry_quantity['values'] = (1,2,3,4,5,6,7,8,9,10)
    entry_quantity['state'] = 'readonly'
    entry_quantity.pack()
    entry_quantity.current(2)

    frame4 = tk.Frame(frejm)
    entryquantity(None,n,frame4)
    entry_quantity.bind('<<ComboboxSelected>>',lambda event: entryquantity(event, n,frame4)) 
    create_graph_button = tk.Button(frejm,text="Utwórz Wykres",command=lambda: create_graph(entry_title,n))
    create_graph_button.pack()
    



