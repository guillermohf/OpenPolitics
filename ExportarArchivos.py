import xlsxwriter
#import pypdf

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
        """
        Se utilizara la libreria de python llamada pypdf,
        la cual se basara en la exportacion que el crawler recopilara de la 
        internet, y lo exportara a excel para una visualizacion mas facil.
        """
        pass
    def OutputEXCEL():
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

