import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from see_graphs import *
import os 
entry_x = {}
entry_y = {}
label_x_y = {}
frame_quantity = {}
def create_graph(name_axis_x,name_axis_y,entry_title,n,username,var):
    print(name_axis_x.get())
    print("Drukuje dlugosc tablicy")
    print("Drukuje wartosc",var.get())
    values_array_x=[]
    values_array_y=[]
    for x in range (n.get()):
        values_array_x.append(int(entry_x[x].get()))
        values_array_y.append(int(entry_y[x].get()))
    
    min_x = int(min(values_array_x))
    min_y = int(min(values_array_y))
    max_x = int(max(values_array_x))
    max_y = int(max(values_array_y))
    min_x = min_x-1
    max_x = max_x+1
    min_y = min_y-1
    max_y = max_y+1
    
    if(var.get()=='0'):
        plt.ylim(0,max_y+2)
        plt.xlim(0,max_x+2)
        
    else:
        plt.ylim(min_y-2,max_y+2)
        plt.xlim(min_x-2,max_x+2)
        
    
    plt.plot(values_array_x,values_array_y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
  
       
    
    plt.xlabel(name_axis_x.get())
    plt.ylabel(name_axis_y.get())
    plt.title(entry_title.get())
    path_of_file = os.getcwd()+ '\\' + username
     
    plt.rcParams["savefig.directory"] = path_of_file
    filename = path_of_file + '\\' + entry_title.get() + '.png'
    plt.savefig(filename)
    plt.show()
def entryquantity(event_or_value,n,frame4):
    

    for widget in frame4.winfo_children():
       widget.destroy()
       
    
    for x in range(n.get()):           
        print(x)
        frame_quantity[x]=tk.Frame(frame4)
        entry_x[x]= tk.Entry(frame_quantity[x],width=2)
        entry_y[x]=tk.Entry(frame_quantity[x],width=2)
        subscript_numbers = "₀₁₂₃₄₅₆₇₈₉"
        subscript_x = subscript_numbers[x]
        text1 = f'x{subscript_x} y{subscript_x}'
        label_x_y=tk.Label(frame_quantity[x],width=3,text=text1)
        label_x_y.pack(side=tk.TOP)
        entry_x[x].pack(side=tk.LEFT)
        entry_y[x].pack(side=tk.RIGHT)
        frame4.pack()
        frame_quantity[x].pack()
        
        

def dot_plot(frejm,username):
    
    
   
    for widget in frejm.winfo_children():
        widget.destroy()
    frejm.pack()
    title=tk.Label(frejm,text="Wpisz Tytuł")
    title.pack()
    entry_title = tk.Entry(frejm)
    entry_title.pack()
    n = tk.IntVar()
    var=tk.StringVar()
    var.set(None)
    name_axis_x_label = tk.Label(frejm,text="Opis linii x")
    begin_coordinate_system = tk.Label(frejm,text="Początek układu współrzędnych")
   
    name_axis_y_label = tk.Label(frejm,text="Opis linii y")
    name_axis_x = tk.Entry(frejm)
    name_axis_y = tk.Entry(frejm)
    name_axis_x_label.pack()
    name_axis_x.pack()
    name_axis_y_label.pack()
    name_axis_y.pack()
    begin_coordinate_system.pack()
    tk.Radiobutton(frejm,value='0',text='Statyczny 0,0',variable=var).pack()
    tk.Radiobutton(frejm,value='1',text='Dynamiczny',variable=var).pack()
    tk.Radiobutton(frejm,value='1',text='Dynamiczny',variable=var).deselect()
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
    create_graph_button = tk.Button(frejm,text="Utwórz Wykres",command=lambda: create_graph(name_axis_x,name_axis_y,entry_title,n,username,var))
    see_graphs_button=tk.Button(frejm, text="Zobacz swoje wykresy",command=lambda: see_graphs(username))
    see_graphs_button.pack()
    create_graph_button.pack()
    
        
