from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from __urls import *
from ElementosEncontrados import *
#Titulo de la ventana
tituloVentana = "Crawler Pais Posible"
root = Tk()
root.title(tituloVentana)
frame = Frame(root, width=450, height=550)
frame.pack()
image = "imagenes\logo2x.jpg"
img = ImageTk.PhotoImage(Image.open(image))
panel = ttk.Label(root, image = img)
panel.place(x=25, y=0)
variable = StringVar(root)
variable.set(list(Sitios__web.keys())[0])
w = OptionMenu(root, variable, *list(Sitios__web.keys()))
w.pack()
Texto1 = Label(root, text="Sitio Web a Buscar: ", font='Helvetica 18 bold')
Texto1.pack()
Texto2 = Label(root, text="Encuestas Encontradas", font='Helvetica 18 bold')
Texto2.pack()
Texto3 = Label(root, text="Mostrar en: ", font='Helvetica 18 bold')
Texto3.pack()
Texto5 = ttk.Button(root, text="Buscar", command=ElementosEncontrados).place(x=280, y=500)
Texto6 = Label(root, text=ElementosEncontrados)
Texto6.pack()
Texto1.place(x=25, y=360)
Texto2.place(x=25, y=450)
Texto3.place(x=25, y=400)
Texto6.place(x=350, y=460)
w.place(x=280, y=360)
v = IntVar()
SeleccionMostrar1 = Radiobutton(root, text="PDF", variable=v, value=1).place(x=280, y=410)
SeleccionMostrar2 = Radiobutton(root, text="EXCEL", variable=v, value=2).place(x=330, y=410)
ttk.Label(root, textvariable="1").place(x=100, y=430)
label = Label(root, text="Version: 0.0.0.1")
label.pack()
mainframe = ttk.Frame(root, padding="13 13 12 12")
root.mainloop()