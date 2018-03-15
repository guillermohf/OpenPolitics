import mysql.connector
#mysql connector for the software to get database

config = {'user': 'root', 'host': '127.0.0.1','database': 'prueba'}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

#DB_NAME = 'PaisPosiblePython'

NombreTabla = "Prueba"
NombreTabla1 = 5
NombreTabla2 = 98
#comando para crear tabla y 
#comandoCrearTabla = "CREATE TABLE {} ({} VARCHAR(20), {} VARCHAR(20))".format(NombreTabla, NombreTabla1, NombreTabla2)
comandoInsertarDatosTabla = "INSERT INTO {} VALUES ({}, {})".format(NombreTabla1, NombreTabla1, NombreTabla2)
#comandoSeleccionarDatosTabla = "SELECT"
#INSERT INTO Prueba VALUES(1, 2)
#print(comando)
#crear tabla
#CREATEDATABASEMYSQL = cursor.execute("CREATE DATABASE PaisPosible_EncuestasHoy")
#SELECTDATABASE = cursor.execute("SELECT * FROM hola")
#creartablepython = cursor.execute(comandoCrearTabla)
InsertarPython = cursor.execute(comandoInsertarDatosTabla)
#CREATETABLEMYSQL

cursor.close()
cnx.close()

        


