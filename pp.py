import requests
from bs4 import BeautifulSoup
import __urls

class CrawlerRefinadoOOP:
    def __init__(self,AskURL, url, Pages, Titulo, Texto, InformacionTitulo, InformacionTexto):
        self.AskURL = AskURL
        self.url = url
        self.Pages = Pages
        self.Titulo = Titulo
        self.Texto = Texto
        self.InformacionTitulo = InformacionTitulo
        self.InformacionTexto = InformacionTexto
    def AskURL(UrlSuperTexto):
        urlTexto = UrlSuperTexto
    def url(self, url):
    #Funcion para llamar a la url, por motivos del crawler
        urlTexto = "http://www." + self.url
    def Item(self, Pages):
        pass
        def CrawlerBuscando():
            Respuestas1 = []
            Respuestas2 = []
            for url in pages:
                r = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")
                RespuestasEncuestas = soup.select(".wp-polls-ans")
            def SuperResultadosEncuestas():
                ResultadosEncuestas = soup.findAll("p", {"class": "titleOnePollGBH"})
            for div in ResultadosEncuestas:
                return Respuestas1.append("{}".format(div.text))
                return Respuestas1
            for div1 in RespuestasEncuestas:
                return Respuestas2.append("{}".format(div1.text))
                return Respuestas2
    def PeriodicoHoy():
        pages = []
        for i in range(1, 105):
            url = 'http://hoy.com.do/encuestas/' + "?poll_page=" + str(i)
            pages.append(url)
        __Titulo = []
        __texto = []
        r = requests.get(pages)
        soup = r.content
        TITULO = soup.select(".wp-polls-ans")
        TEXTOS = soup.findAll("p", {"class": "titleOnePollGBH"})
        for __items in TITULO:
            return __titulo.append("{}".format(__items.text))
            print(__titulo)

CR = CrawlerRefinadoOOP.PeriodicoHoy()
print(CR)

import xlsxwriter
import pypdf

class Crawler_Encuestas:
    """
        Esta clase lo que se encargara de llamar al requests y al beautifulsoup
        que son librerias en python, su funcion es buscar los resultados y el titulo
        y habra una clase al final que se encargara de hacer un output en excel o pdf
        o en la misma ventana.
    """
    def __init__(self, Output):
        self.Output = Output

    def OutputPDF(self):
        """
        Se utilizara la libreria de python llamada pypdf,
        la cual se basara en la exportacion que el crawler recopilara de la 
        internet, y lo exportara a excel para una visualizacion mas facil.
        """
        pass
    def OutputEXCEL(self):
        """
        Se utilizara el xlsxwriter para el Output de la informacion captada
        por el crawler, que tambien mostrara graficas.
        """
        try:
            workbook = xlsxwriter.Workbook('hello.xlsx')
            worksheet = workbook.add_worksheet()
            worksheet.write('A1', 'Hello world')
            workbook.close()
        except ValueError:
            pass
