from tkinter import *
from tkinter import ttk
from PIL import ImageTK, Image

root = Tk()
root.title(tituloVentana)
frame = Frame(root, width=450, height=550)
frame.pack()
image = "logo2x.jpg"
img = ImageTk.PhotoImage(Image.open(image))
panel = ttk.Label(root, image = img)
panel.place(x=25, y=0)