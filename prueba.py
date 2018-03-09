import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()

""""
def Listin_Diario():
    def La_Informacion():
        print("nada")
    def Telenoticias():
    def El_dinero():
    def Diario_55():
    def La_bazuca():
    def Primicias():
    def CDN():
    def El_Informador():
    def El_Nacional():
    def El_Caribe():
    def El_Nuevo_Diario():
    def El_Dia():
    def Diario_Libre():
    def Noticias_RD():
        """"