import os
import cv2
import matplotlib.pyplot as plt
from matplotlib.image import imread
#path
import glob
# Importing Essentials
import os
from tkinter import Tk, Label, PhotoImage

# Initialize Tk root Class
root = Tk()

# Set Default Size of Our Tkinter Window - (WidthxHeight)
root.geometry("200x910")

# Set Minimum Size of Our Window - (Width, Height)
root.minsize(350, 200)

# Add a Label
WelcomeLabel = Label(text="All Images of This Folder")
WelcomeLabel.grid(row=0)

# Get All PNG Files in a List name pngFiles
pngFiles = []
for item in os.listdir():
    if item.endswith(".png"):
        pngFiles.append(item)
print(pngFiles)
# Display All The PNG files to our GUI Screen
i = 0
pics = []
for file in pngFiles:
    pics.append(PhotoImage(file=file))
    Label(root, image=pics[i]).grid(row=i + 1)
    i += 1

# Run The MainLoop
root.mainloop()
"""from IPython.display import Image, display
for imageName in glob.glob('aaa/*.png'): #assuming JPG
    display(Image(filename=imageName))
    print(imageName)"""






"""folder = 'aaa/'
for i in range(9):
    # define subplot
    plt.subplot(330 + 1 + i)
    x= folder + 'cat.' + str(i) + '.png'
    # load image pixels
    image = imread(x)
    # plot raw pixel data
    plt.imshow(image)

plt.show()"""
"""path='aaa'
images=os.listdir(path)
type(images)
print(len(images))
img_data=[]
for img in images:
    img_arr=cv2.imread(os.path.join(path,img))
    img_data.append(img_arr)
    plt.figure()
    plt.imshow(img_arr)
plt.figure(figsize=(10,10))
for i in range(len(img_data)):
    plt.subplot(6,4,i+1)
    plt.imshow(img_data[i])

#plt.show() """
