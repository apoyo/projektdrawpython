import os
import tkinter as tk
from tkinter import Tk, Label, Button, filedialog,Toplevel
from PIL import Image, ImageTk
import keyboard



image_files=[]
current_image_index = 0
image_label = None
username = None

def next_image():
         global current_image_index, image_files
         if image_files:
              current_image_index = (current_image_index + 1) % len(image_files)
              show_image()
def previous_image():
          global current_image_index, image_files
          if image_files:
              current_image_index = (current_image_index - 1) % len(image_files)
              show_image()

def show_image():
      global current_image_index,image_files,image_label
      print("Current Image Index",current_image_index)
      if image_files:
              
              image_path = image_files[current_image_index]
              image = Image.open(image_path)
              
              image.thumbnail((800, 600)) 
                         
              photo = ImageTk.PhotoImage(image)
              image_label.config(image=photo)
              image_label.image = photo
        
      else:
             image_label.config(text="Brak zdjęć w folderze")

def see_graphs(username):
    
    root2 = Toplevel()
    root2.geometry("800x600")
    root2.title("Moje wykresy")
    global image_label,image_files,current_image_index
    image_label =  Label(root2)
    image_label.pack()
    #keyboard.on_press_key('right',lambda event: next_image())
    #keyboard.on_press_key('left',lambda event: previous_image())
    next_button = Button(root2,text="Następny",command=next_image)
    previous_button = Button(root2,text="Poprzedni",command=previous_image)
    root2.bind("<Right>",lambda event: next_image() )
    root2.bind("<Left>", lambda event: previous_image())
    next_button.pack(side='right',fill="both",expand=True)
    previous_button.pack(side='left',fill="both",expand=True)
   
    folder_path=os.getcwd()+ '\\' + username
    
    if folder_path:
        image_files = [
            os.path.join(folder_path,f)
            for f in os.listdir(folder_path)
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))
            
        ]
        
    print(image_files)
    show_image()
    root2.mainloop()
   

