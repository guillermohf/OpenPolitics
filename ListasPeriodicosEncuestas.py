import requests
from bs4 import BeautifulSoup

class PeriodicosEncuestas:
    """
        Periodicos de las encuestas con su metodo definido
    """
    def __init__(self, Hoy):
        self.Hoy = Hoy
    def Hoy():
        url = "http://hoy.com.do/encuestas/"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "lxml")
        TituloNoticia = soup.find_all("strong")
        ResultadosEncuestas = soup.findAll("ul", {"class": "wp-polls-ul"})
        for div in ResultadosEncuestas:
                print(div)
        #print(TituloNoticia)
        #print("------")
        #print(ResultadosEncuestas[1])
    

PEHOY = PeriodicosEncuestas.Hoy()

#opciones de sitios web a buscar
Hoy = "Hoy"
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


