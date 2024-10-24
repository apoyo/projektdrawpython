import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry("500x500")

root.title("Rysowanie Wykresów")

#image = Image.open("graph.png")
#resize_image =  image.resize((100,100))
#img =  ImageTk.PhotoImage(resize_image)
#image_label = Label(image=img)
#image_label.image = img
#image_label.grid(row=0,column=0,padx=(10, 100),pady=(10,100))

#image_label.pack(side="left", fill="both", expand=False)
#image_label.place(x=200, y=200, height=100, width=100)

#pack, place ,grid


root.configure(bg='#333333')
label = tk.Label(root,text = "Logowanie",font=('Arial',30),bg='#333333',fg='#FFFFFF' )
label.grid(row=0,column=2,sticky="news",columnspan=2,pady=40)
myLabelLogin = tk.Label(root,text = "Login",bg='#333333',fg='#FFFFFF',font=('Arial',16) )
myEntryLogin = tk.Entry(root,font=('Arial',16) )
myEntryPassword = tk.Entry (root,show="*",font=('Arial',16))
myLabelPassword = tk.Label (root,text="Password",bg='#333333',fg='#FFFFFF',font=('Arial',16) )
loginButton = tk.Button(root, text='Zaloguj' ,font =('Arial',18),bg="#FF3399",fg="#FFFFFF")
myLabelLogin.grid(row=1,column=1)
myLabelPassword.grid(row=2,column=1)
myEntryLogin.grid(row=1,column=2,pady=20)
myEntryPassword.grid(row=2,column=2,pady=20)
loginButton.grid(row=3,column=2)

#myEntryLogin.pack(padx=3,pady=3)
#myEntryPassword.pack(padx=3,pady=3)



#loginButton.pack()


inputtxt = tk.Text(root, height=3)
#inputtxt.pack(padx=10,pady=10)

myEntry = tk.Entry(root)
#myEntry.pack()

button = tk.Button(root, text="Click Me!", font = ('Arial', 18 ))

#button.pack(padx=10,pady=10)

root.mainloop()
