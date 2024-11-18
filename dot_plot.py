import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk

def entryquantity(event_or_value,n,frame4):
    print('Klantity dziala')
    
    for widget in frame4.winfo_children():
        widget.destroy()
    for x in range(n.get()):           
        print(x)
        x = tk.Entry(frame4)
        x.pack()
        frame4.pack()

def dot_plot(frejm):
    
    print('Wykres punktowy')
    #root = tk.Tk()
    #root.geometry("500x500")
    #root.title("Nie rysowanie Wykresów")
    #label = tk.Label(root,text = "Cokolwiek xd",font=('Arial',30),bg='#333333',fg='#FFFFFF' )
    #label.pack(pady=40)
    #frejm= tk.Frame(bg='#FFFFFF')
    #frejm.pack_forget()
    for widget in frejm.winfo_children():
        widget.destroy()
    frejm.pack()
    title=tk.Label(frejm,text="Wpisz Tytuł")
    title.pack()
    entry_title = tk.Entry(frejm)
    entry_title.pack()
    n = tk.IntVar()
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
    

    
        
    #xpoints = np.array([1, 8])
    #ypoints = np.array([3, 10])
    
    #plt.plot(xpoints, ypoints)
    #plt.show()
