from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
from PIL import ImageTk, Image
import xlsxwriter

root = Tk()
root.title("Buscador de encuestas Pais Posible")
frame = Frame(root, width=450, height=550)
frame.pack()
image = "logo2x.jpg"
img = ImageTk.PhotoImage(Image.open(image))
panel = ttk.Label(root, image = img)
panel.place(x=25, y=0)

#Colocarle el icono de imagen de la aplicacion
#root.iconphoto(root, PhotoImage(file="logo2x.jpg"))

#encuestas encontradas
def ScrapingInformacion():
    "Scraping Prueba"
    try:
        print("Scraping Prueba")
    except ValueError:
        pass

#opciones de sitios web a buscar
Hoy = "Hoy*"
Listin_Diario = "Listin Diario*"
La_Informacion = "La Informacion*"
Telenoticias = "Telenoticias*"
El_dinero = "El Dinero*"
Diario_55 = "Diario 55*"
La_bazuca = "La Bazuca*"
Primicias = "Primicias*"
CDN = "CDN*"
El_Informador = "El Informador*"
El_Nacional  = "El Nacional*"
El_Caribe = "El Caribe*"
El_Nuevo_Diario = "El Nuevo Diario*"
El_Dia = "El Dia*"
Diario_Libre = "Diario Libre*"
Noticias_RD = "Noticias RD*"
PDF = "PDF*"
EXCEL = "EXCEL*"

Sitios_web = [
        Hoy,
    Listin_Diario,
    La_Informacion,
    Telenoticias,
    El_dinero,
    Diario_55,
    La_bazuca,
    Primicias,
    CDN,
    El_Informador,
    El_Nacional,
    El_Caribe,
    El_Nuevo_Diario,
    El_Dia,
    Diario_Libre,
    Noticias_RD
]

class Crawler_Encuestas:
    """
        Esta clase lo que se encargara de llamar al requests y al beautifulsoup
        que son librerias en python, su funcion es buscar los resultados y el titulo
        y habra una clase al final que se encargara de hacer un output en excel o pdf
        o en la misma ventana.
    """
    
    def __init__(self, Output):
        self.Output = Output

    def OutputPDF():

    def OutputEXCEL()
        try:
            workbook = xlsxwriter.Workbook('hello.xlsx')
            worksheet = workbook.add_worksheet()
            worksheet.write('A1', 'Hello world')
            workbook.close()
        except ValueError:
        pass

variable = StringVar(root)
variable.set(Sitios_web[0]) # valor por default

w = OptionMenu(
    root, variable, *Sitios_web
    )
w.pack()

probando = "150"

#Textos A Mostrar
Texto1 = Label(root, text="Sitio Web a Buscar: ", font='Helvetica 18 bold')
Texto1.pack()
Texto2 = Label(root, text="Encuestas Encontradas", font='Helvetica 18 bold')
Texto2.pack()
Texto3 = Label(root, text="Mostrar en: ", font='Helvetica 18 bold')
Texto3.pack()
Texto5 = ttk.Button(root, text="Buscar", command=Crawler_Encuestas.OutputPDF()).place(x=280, y=500)
Texto6 = Label(root, text=probando)
Texto6.pack()
#Posiciones
Texto1.place(x=25, y=360)
Texto2.place(x=25, y=450)
Texto3.place(x=25, y=400)
Texto6.place(x=350, y=460)
#Texto4.place(x=25, y=340)
w.place(x=280, y=360)
#Mostrar en pdf o excel en la ventana de mostrar resultados
v = IntVar()
SeleccionMostrar1 = Radiobutton(root, text=PDF, variable=v, value=1).place(x=280, y=410)
SeleccionMostrar2 = Radiobutton(root, text=EXCEL, variable=v, value=2).place(x=330, y=410)

#
ttk.Label(root, textvariable="1").place(x=100, y=430)


label = Label(root, text="Version: 0.0.0.1")
label.pack()
mainframe = ttk.Frame(root, padding="13 13 12 12")
root.mainloop()