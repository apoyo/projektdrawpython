import os
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Przeglądarka obrazów")
        
        self.image_label = Label(root)
        self.image_label.pack()
        
        self.next_button = Button(root, text="Następny", command=self.next_image)
        self.next_button.pack()

        self.prev_button = Button(root, text="Poprzedni", command=self.prev_image)
        self.prev_button.pack()

        self.image_files = []
        self.current_image_index = 0
   
    def show_image(self):
        image_path = self.image_files[self.current_image_index]
        image = Image.open(image_path)
        image.thumbnail((800, 600))  # Dopasuj rozmiar obrazu do okna
        photo = ImageTk.PhotoImage(image)

        self.image_label.config(image=photo)
        self.image_label.image = photo  # Trzeba przypisać referencję, aby obraz się wyświetlił

    def next_image(self):
        if self.image_files:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_files)
            self.show_image()

    def prev_image(self):
        if self.image_files:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_files)
            self.show_image()

if __name__ == "__main__":
    root = Tk()
    viewer = ImageViewer(root)
    root.mainloop()

