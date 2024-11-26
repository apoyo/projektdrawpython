import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import os

print(os.getcwd())  # Wyświetla bieżący katalog roboczy
print(glob.glob('./aaa/*.png'))  # Wyświetla listę znalezionych obrazów
images = []
for img_path in glob.glob('./aaa/*.png'):
    images.append(mpimg.imread(img_path))

plt.figure(figsize=(20,10))
columns = 4
for i, image in enumerate(images):
    plt.subplot(len(images) / columns + 1, columns, i + 1)
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])

plt.show()