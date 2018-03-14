from tkinter import * #Imports Tkinter
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk, Canvas, Frame, BOTH
import sys #Imports sys, used to end the program later
from PIL import ImageTk, Image
from __urls import *
from ElementosEncontrados import *


##
firstclick = True
SecondClick = True
ThirdClick = True

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

root = Tk() #Declares root as the tkinter main window
top = Toplevel() #Creates the toplevel window
###
#Titulo de la ventana
tituloVentana = "Crawler Pais Posible"
root.title(tituloVentana)
TituloVentanaLogin = "Autentificacion"
top.title(TituloVentanaLogin)
AnchoVentana = root.winfo_screenwidth()
AlturaVentana = root.winfo_screenheight()
frame = Frame(root, width=AnchoVentana, height=AlturaVentana)
frame2 = Frame(top, width=300,height=250)
coordenada_x = ((AnchoVentana/2))
coordenada_y = (AlturaVentana/2)
frame.pack()
frame2.pack()
image = "imagenes\logo3x.jpg"
img = ImageTk.PhotoImage(Image.open(image))
panel = ttk.Label(root, image = img)
panel2 = ttk.Label(top, image = img)
panel2.place(x=150, y=100, anchor=CENTER)
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
IntroducirPalabraBuscar.bind('<FocusIn>', on_entry_click)
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
#

##
Usuario = Entry(top) #usuario
Usuario.insert(0, "Usuario")
Usuario.bind('<FocusIn>', on_entry_click)
contraseña = Entry(top, show="*") #contraseña
contraseña.insert(0, "Contraseña")
contraseña.bind('<FocusIn>', on_entry_click)
Validar = "Conectar"
Cancelar = "Cancelar"
button1 = Button(top, text=Validar, command=lambda:command1()) #Login button
button2 = Button(top, text=Cancelar, command=lambda:command2()) #Cancel button

def command1():
    if Usuario.get() == "morrison" and contraseña.get() == "morrison": #Checks whether username and password are correct
        root.deiconify() #Unhides the root window
        top.destroy() #Removes the toplevel window
    else:
        messagebox.showinfo("Usuario o Contraseña incorrecta!", "Por favor colocar usuario o contraseña correctamente de lo contrario contactarse con el administrador.")

def command2():
    top.destroy() #Removes the toplevel window
    root.destroy() #Removes the hidden root window
    sys.exit() #Ends the script


Usuario.place(x = 20, y = 170) #These pack the elements, this includes the items for the main window
contraseña.place(x = 150, y = 170)
button1.place(x = 90, y = 200)
button2.place(x = 150, y = 200)

root.withdraw() #This hides the main window, it's still present it just can't be seen or interacted with
root.mainloop() #Starts the event loop for the main window