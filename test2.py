import tkinter as tk
from tkinter import Label
import numpy as np
from PIL import Image, ImageTk

root = tk.Tk()

# create label1 with an image
image = Image.open('images/empty.png')
image = image.resize((500, 750), Image.ANTIALIAS)
picture = ImageTk.PhotoImage(image=image)
label1 = Label(root, image=picture)
label1.image = picture

# extract rgb from image of label1
width, height = label1.image._PhotoImage__size
rgb = np.empty((height, width, 3))
for j in range(height):
    for i in range(width):
        rgb[j, i, :] = label1.image._PhotoImage__photo.get(x=i, y=j)

# create new image from rgb, resize and use for label2
new_image = Image.fromarray(rgb.astype('uint8'))
new_image = new_image.resize((250, 300), Image.ANTIALIAS)
picture2 = ImageTk.PhotoImage(image=new_image)
label2 = Label(root, image=picture2)
label2.image = picture2

# grid the two labels
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)

root.mainloop()