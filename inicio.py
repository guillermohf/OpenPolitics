from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from __urls import *
from ElementosEncontrados import *
#Titulo de la ventana
tituloVentana = "Crawler Pais Posible"
root = Tk()
root.title(tituloVentana)
AnchoVentana = root.winfo_screenwidth()
AlturaVentana = root.winfo_screenheight()
frame = Frame(root, width=AnchoVentana, height=AlturaVentana)
coordenada_x = ((AnchoVentana/2))
coordenada_y = (AlturaVentana/2)
frame.pack()
image = "imagenes\logo3x.jpg"
img = ImageTk.PhotoImage(Image.open(image))
panel = ttk.Label(root, image = img)
panel.place(x=coordenada_x, y=75, anchor=CENTER)
variable = StringVar(root)
variable.set(list(Sitios__web.keys())[0])
w = OptionMenu(root, variable, *list(Sitios__web.keys()))
w.pack()
#keyword
IntroducirPalabraBuscar = Entry(root)
IntroducirPalabraBuscar.pack()
PalabraIntroducirDemo = "Palabra Busqueda"
IntroducirPalabraBuscar.insert(0, PalabraIntroducirDemo)
IntroducirPalabraBuscar.place(x=920, y=100, anchor=CENTER)
F = StringVar()
F.set(PalabraIntroducirDemo)
IPB = F.get()
Texto1 = Label(root, text="Keyword: ", font='Helvetica 18 bold')
Texto1.pack()
Texto2 = Label(root, text="Encuestas Encontradas:", font='Helvetica 18 bold')
Texto2.pack()
Texto5 = ttk.Button(root, text="Buscar", command=ElementosEncontrados).place(x=360, y=410)
Texto6 = Label(root, text=ElementosEncontrados)
Texto6.pack()
Texto1.place(x=25, y=360)
Texto2.place(x=25, y=400)
Texto6.place(x=325, y=410)
w.place(x=280, y=360)
v = IntVar()
ttk.Label(root, textvariable="1").place(x=100, y=430)
Version = "0.0.0.2"
label = Label(root, text=Version)
label.pack()
mainframe = ttk.Frame(root)
root.mainloop()
