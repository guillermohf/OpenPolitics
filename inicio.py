#Third Party imports
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk, Canvas, Frame, BOTH
from PIL import ImageTk, Image
#system imports
import sys
#inner documents imports
from __urls import *
from ElementosEncontrados import *
from UsersAuth import *
#Booleans
firstclick = True
SecondClick = True
ThirdClick = True
#Functions
def on_entry_click(event):
    """function that gets called whenever entry1 is clicked"""        
    global firstclick

    if firstclick: # if this is the first time they clicked it
        firstclick = False
        Usuario.delete(0, "end") # delete all the text in the entry
    elif SecondClick:
        SecondClick = False
        contraseña.delete(0, "end")
    elif ThirdClick:
        ThirdClick = False
        IntroducirPalabraBuscar.delete(0, "end")
#WhiteListURLS.keys())[0]
def command1():
    if Usuario.get() == list(UsersAuth.keys()) and contraseña.get() == list(UsersAuth.values()): 
        root.deiconify() #Unhides the root window
        top.destroy() #Removes the toplevel window
    else:
        messagebox.showinfo("Usuario o Contraseña incorrecta!", "Por favor colocar usuario o contraseña correctamente de lo contrario contactarse con el administrador.")

def command2():
    top.destroy() #Removes the toplevel window
    root.destroy() #Removes the hidden root window
    sys.exit() #Ends the script
#Files Routes
image = "imagenes\logo3x.jpg"
#Declaring Variables
root = Tk()
top = Toplevel()
tituloVentana = "Crawler Pais Posible"
TituloVentanaLogin = "Autentificacion"
Validar = "Conectar"
Cancelar = "Cancelar"
AnchoVentana = root.winfo_screenwidth()
AlturaVentana = root.winfo_screenheight()
AnchoVentanaLogin = root.winfo_screenwidth()/5
AlturaVentanaLogin = root.winfo_screenheight()/3
variable = StringVar(root)
w = OptionMenu(root, variable, *list(WhiteListURLS.keys()))
Usuario = Entry(top) #usuario
Usuario.insert(0, "Usuario")
Usuario.bind('<FocusIn>', on_entry_click)
contraseña = Entry(top, show="*") #contraseña
contraseña.insert(0, "Contraseña")
contraseña.bind('<FocusIn>', on_entry_click)
Texto1 = Label(root, text="Keyword: ", font='Helvetica 18 bold')
frame = Frame(root, width=AnchoVentana, height=AlturaVentana)
frame2 = Frame(top, width=AnchoVentanaLogin,height=AlturaVentanaLogin)
img = ImageTk.PhotoImage(Image.open(image))
panel = ttk.Label(root, image = img)
panel2 = ttk.Label(top, image = img)
button1 = Button(top, text=Validar, command=lambda:command1()) #Login button
button2 = Button(top, text=Cancelar, command=lambda:command2()) #Cancel button
IntroducirPalabraBuscar = Entry(root)
PalabraIntroducirDemo = "Palabra Busqueda"
F = StringVar()
IPB = F.get()
Texto2 = Label(root, text="Encuestas Encontradas:", font='Helvetica 18 bold')
Texto5 = ttk.Button(root, text="Buscar", command=ElementosEncontrados).place(x=360, y=410)
Version = "0.0.0.3"
label = Label(root, text=Version)
v = IntVar()
Texto6 = Label(root, text=ElementosEncontrados)
#coordinates
coordenada_x = ((AnchoVentana/2))
coordenada_y = (AlturaVentana/2)
#Tkinter commands
root.title(tituloVentana)
top.title(TituloVentanaLogin)
F.set(PalabraIntroducirDemo)
variable.set(list(WhiteListURLS.keys())[0])
IntroducirPalabraBuscar.insert(0, PalabraIntroducirDemo)
IntroducirPalabraBuscar.bind('<FocusIn>', on_entry_click)
#placing
panel2.place(x=150, y=100, anchor=CENTER)
panel.place(x=coordenada_x, y=75, anchor=CENTER)
Usuario.place(x = 20, y = 170) #These pack the elements, this includes the items for the main window
contraseña.place(x = 150, y = 170)
button1.place(x = 90, y = 200)
button2.place(x = 150, y = 200)
Texto1.place(x=25, y=360)
Texto2.place(x=25, y=400)
Texto6.place(x=325, y=410)
IntroducirPalabraBuscar.place(x=920, y=100, anchor=CENTER)
w.place(x=280, y=360)
ttk.Label(root, textvariable="1").place(x=100, y=430)
#pack
w.pack()
Texto1.pack()
frame.pack()
frame2.pack()
Texto2.pack()
IntroducirPalabraBuscar.pack()
label.pack()
Texto6.pack()
#Starting Out Tkinter
root.withdraw()
root.mainloop()