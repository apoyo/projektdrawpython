import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from dot_plot import * 
from bar_chart import *
from line_graph import *
from pie_chart import *
#from PIL import Image, ImageTk
import sqlite3
root = tk.Tk()
root.geometry("500x500")

root.title("Rysowanie Wykresów")
def clearFrame():
    # destroy all widgets from frame
    print("CLIRFREJM")
    for widget in frame.winfo_children():
       widget.destroy()
#image = Image.open("graph.png")
#resize_image =  image.resize((100,100))
#img =  ImageTk.PhotoImage(resize_image)
#image_label = Label(image=img)
#image_label.image = img
#image_label.grid(row=0,column=0,padx=(10, 100),pady=(10,100))

#image_label.pack(side="left", fill="both", expand=False)
#image_label.place(x=200, y=200, height=100, width=100)

#pack, place ,grid




def graphchoosen(event):
    print("Funkcja się uruchamia!")
    if n.get()=="Wykres punktowy":
        #print('Wykres punktowy')
        dot_plot()
    elif n.get()=="Wykres liniowy":
        #print('Wykres liniowy')
        line_graph()
    elif n.get()=="Wykres słupkowy":
        #print('Wykres słupkowy')
        bar_chart()
    else:
        #print('Wykres kołowy')
        pie_chart()

root.configure(bg='#333333') 
def login():
    conn = sqlite3.connect('data.db')
    username = myEntryLogin.get()
    password = myEntryPassword.get()
    table_create_query= '''CREATE TABLE IF NOT EXISTS logins(id INTEGER PRIMARY KEY,login varchar(25),password varchar(15),last_seen date ) '''
    conn.execute(table_create_query)
    cursorone = conn.cursor()
    query_one = '''SELECT login from logins where login= ?'''
    cursorone.execute(query_one,(username,))
    #conn.commit()
    result =  cursorone.fetchone()
    print(result)
    if result:
        print("Przechodzi")
        cursortwo = conn.cursor()
        query_two = '''SELECT password from logins where login=?'''
        cursortwo.execute(query_two,(username,))
        result_final = cursortwo.fetchone()[0]
      
        print(result_final)
        if result_final==password:
           print("Jestesmy w miejscu docelowym")
           messagebox.showinfo(title="info",message="Jestes Zalogowany")
           frame.destroy()
           print("FINAL PACK")
           root.configure(bg='#FFFFFF') 
           frame_final.pack()
           graphchoosen(Event)
           

        else:
           messagebox.showinfo(title="info",message="Haslo jest nieprawidłowe")
     
    else:
        confirm = messagebox.askyesno(title="",message="Brak konta czy chcesz je założyć ?")
        print(confirm)
        if confirm:
             insert_query ='''INSERT INTO logins (login,password) VALUES(?,?)'''
             print("dodaje_raz")
             insert_tuple = (myEntryLogin.get(),myEntryPassword.get())
             cursor = conn.cursor()
             cursor.execute(insert_query,insert_tuple)
             conn.commit()
             messagebox.showinfo(title="info",message="Jestes Zalogowany")
             frame.destroy()
             root.configure(bg='#FFFFFF') 
             frame_final.pack()
             if(graphchoose.get()=='Wykres liniowy'):
                 print("Wykres Liniowy")
        else:
            messagebox.showinfo(title="Kursor",message= 'Nie załozono konta')
             
    
    #password = ''''''
    #if(myEntryLogin.get()== ,myEntryPassword.get()== )

    conn.close()
     
   
    #if myEntryLogin.get()==username and myEntryPassword.get()==password:
     #   messagebox.showinfo(title="Login Success",message="Tou successfully logged in.")
        #print("Successfully logged in")
    #else:
    #   messagebox.showinfo(title="Error",message="Invalid")
    #  print("Invalid login")


#frame2 = tk.Frame(bg='#333333')
#label2 = tk.Label(frame,text = "LOgowanie DWA",font=('Arial',30),bg='#333333',fg='#FFFFFF' )
#label2.grid(row=0,column=2,sticky="news",columnspan=2,pady=40)
frame= tk.Frame(bg='#333333')
frame_final = tk.Frame(bg='#FFFFFF')
label = tk.Label(frame,text = "Logowanie",font=('Arial',30),bg='#333333',fg='#FFFFFF' )
label.grid(row=0,column=2,sticky="news",columnspan=2,pady=40)
myLabelLogin = tk.Label(frame,text = "Login",bg='#333333',fg='#FFFFFF',font=('Arial',16) )
myEntryLogin = tk.Entry(frame,font=('Arial',16) )
myEntryPassword = tk.Entry (frame,show="*",font=('Arial',16))
myLabelPassword = tk.Label (frame,text="Password",bg='#333333',fg='#FFFFFF',font=('Arial',16) )
loginButton = tk.Button(frame, text='Zaloguj' ,font =('Arial',18),bg="#FF3399",fg="#FFFFFF",command=login)
myLabelLogin.grid(row=1,column=1)
myLabelPassword.grid(row=2,column=1)
myEntryLogin.grid(row=1,column=2,pady=20)
myEntryPassword.grid(row=2,column=2,pady=20)
loginButton.grid(row=3,column=2,columnspan=2,pady=30)
#graphType = tk.Listbox(frame_final)
#graphType.insert(1,"Python")
#graphType.insert(2,"Python")
#myEntryLogin.pack(padx=3,pady=3)
#myEntryPassword.pack(padx=3,pady=3)

#graphtype = Listbox(frame_final,)

#loginButton.pack()
n = tk.StringVar()
graphchoose = ttk.Combobox(frame_final ,width=27, textvariable = n )
graphchoose['values'] = ('Wykres liniowy','Wykres punktowy','Wykres słupkowy','Wykres kołowy')
graphchoose['state'] = 'readonly'
graphchoose.grid(column = 1, row = 5) 
graphchoose.current(1) 

inputtxt = tk.Text(frame, height=3)
#inputtxt.pack(padx=10,pady=10)

myEntry = tk.Entry(frame)
#myEntry.pack()

button = tk.Button(frame, text="Click Me!", font = ('Arial', 18 ))

#button.pack(padx=10,pady=10)
frame.pack()


def newwindow():
    frame.pack_forget()

graphchoose.bind('<<ComboboxSelected>>',graphchoosen)
root.mainloop()

