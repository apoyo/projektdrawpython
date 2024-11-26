import os
import cv2
import matplotlib.pyplot as plt
from matplotlib.image import imread
#path
import glob
# Importing Essentials

"""from IPython.display import Image, display
for imageName in glob.glob('aaa/*.png'): #assuming JPG
    display(Image(filename=imageName))
    print(imageName)"""

import pathlib
from tkinter import Tk, Label, PhotoImage

root = Tk()
root.geometry("200x910")
root.minsize(350, 200)

wellcome = Label(text="All Images of This Folder")
wellcome.pack()

# create a list from images with memory reference
images_with_ref = []
for img in pathlib.Path('.').glob('*.png'):
    photoLoaded = PhotoImage(file=img)
    images_with_ref.append(photoLoaded)

# create labels with correct images
for image in images_with_ref:
    Label(image=image).pack()

root.mainloop()




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
