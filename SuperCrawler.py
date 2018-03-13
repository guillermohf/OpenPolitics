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
        url = "hoy.com.do/encuestas"
        r = requests.get(pages)
        soup = r.content
        TITULO = soup.select(".wp-polls-ans")
        TEXTOS = soup.findAll("p", {"class": "titleOnePollGBH"})
        for __items in TITULO:
            return __titulo.append("{}".format(__items.text))
            print(__titulo)

CR = CrawlerRefinadoOOP.PeriodicoHoy()
print(CR)

