import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import ExportarArchivos
import ListasPeriodicosEncuestas
import requests
from bs4 import BeautifulSoup
import sys
import xlsxwriter
#import pypdf
pages = []
#
Respuestas1 = []
Respuestas2 = []
for i in range(1, 105):
    url = 'http://hoy.com.do/encuestas/' + "?poll_page=" + str(i)
    pages.append(url)


#sitios Web
class PeriodicosEncuestas:
    def __init__(self, Hoy):
        self.Hoy = Hoy
    def HoyTitulo():
    #def get_data_from_url(url):
    #   for i in range(106):
    #      print(url_2)
    #r = requests.get(pages)
        for item in pages:
            page = requests.get(item)
            soup = BeautifulSoup(page.content, "lxml")
            ResultadosEncuestas = soup.findAll("p", {"class": "titleOnePollGBH"})
        for div in ResultadosEncuestas:
            Respuestas1.append("%s" %(div.text))

    def HoyTexto():
        for item in pages:
            page = requests.get(item)
            soup = BeautifulSoup(page.content, "lxml")
            RespuestasEncuestas = soup.select(".wp-polls-ans")
        for div1 in RespuestasEncuestas:
            return Respuestas2.append("%s" %(div1.text))
            print(Respuestas2)

PE = PeriodicosEncuestas.HoyTexto()