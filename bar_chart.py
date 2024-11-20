from dot_plot import * 
from bar_chart import *
from pie_chart import *
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
entry_x = {}
entry_y = {}
entry_tick_label = {}
label_x_y = {}
frame_quantity = {}
def create_graph(name_axis_x,name_axis_y,entry_title,n):
    print(name_axis_x.get())
    print("Drukuje dlugosc tablicy")
    values_array_x=[]
    values_array_y=[]
    values_label=[]
    for x in range (n.get()):
        values_array_x.append(entry_x[x].get())
        values_array_y.append(int(entry_y[x].get()))
        values_label.append(entry_tick_label[x].get())
    print(values_array_x)
    print('Maksymalny x',max(values_array_x))
    print('Zawartosc tablic')
    print(values_array_x,values_array_y)
    plt.bar(values_array_x,values_array_y,tick_label = values_label,width=0.8, color=['red','green'])
    
    #plt.ylim(min_y-2,max_y+2)
    #plt.xlim(min_x-2,max_x+2)
    plt.xlabel(name_axis_x.get())
    plt.ylabel(name_axis_y.get())
    plt.title(entry_title.get())
    plt.show()
def entryquantity(event_or_value,n,frame4):
    print('Klantity dziala')

    for widget in frame4.winfo_children():
       widget.destroy()
    for x in range(n.get()):           
        print(x)
        frame_quantity[x]=tk.Frame(frame4)
        entry_x[x]= tk.Entry(frame_quantity[x],width=2)
        entry_y[x]=tk.Entry(frame_quantity[x],width=2)
        label_x=tk.Label(frame_quantity[x],width=2,text="Lewa strona słupka")
        label_y=tk.Label(frame_quantity[x],width=2,text="Prawa strona słupka")
        tick_label = tk.Label(frame_quantity[x],width=5,text="Etykieta")
        entry_tick_label[x] = tk.Entry(frame_quantity[x],width=5)
        label_x.pack(side=tk.LEFT)
        label_y.pack(side=tk.RIGHT)
        entry_x[x].pack(side=tk.LEFT)
        entry_y[x].pack(side=tk.RIGHT)
        tick_label.pack()
        entry_tick_label[x].pack()
     
        frame4.pack()
        frame_quantity[x].pack()




def bar_chart(frejm):
    print('Wykres słupkowy')
    for widget in frejm.winfo_children():
        widget.destroy()
   
    frejm.pack()
    title=tk.Label(frejm,text="Wpisz Tytuł")
    title.pack()
    entry_title = tk.Entry(frejm)
    entry_title.pack()
    n = tk.IntVar()

    name_axis_x_label = tk.Label(frejm,text="Opis osi x")
    name_axis_y_label = tk.Label(frejm,text="Opis osi y")
    name_axis_x = tk.Entry(frejm)
    name_axis_y = tk.Entry(frejm)
    name_axis_x_label.pack()
    name_axis_x.pack()
    name_axis_y_label.pack()
    name_axis_y.pack()
    entry_quantity_label = tk.Label(frejm,text="Liczba przycisków")
    entry_quantity_label.pack()

    entry_quantity=ttk.Combobox(frejm,width=5, textvariable = n )
    entry_quantity['values'] = (1,2,3,4,5,6,7,8,9,10)
    entry_quantity['state'] = 'readonly'
    entry_quantity.pack()
    entry_quantity.current(2)

    #frame_graph=tk.Frame(bg='#FFFFFF')
    #entry1 = tk.Entry(frejm)
    #ntry2 = tk.Entry(frejm)
    #entry1.pack()
    #entry2.pack()
    frame4 = tk.Frame(frejm)
    entryquantity(None,n,frame4)
    entry_quantity.bind('<<ComboboxSelected>>',lambda event: entryquantity(event, n,frame4)) 
    create_graph_button = tk.Button(frejm,text="Utwórz Wykres",command=lambda: create_graph(name_axis_x,name_axis_y,entry_title,n))
    create_graph_button.pack()
    
    