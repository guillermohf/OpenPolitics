import mysql.connector

config = {
    'user': 'root',
    'host': '127.0.0.1',
    'database': 'PaisPosiblePython'
}

cnx = mysql.connector.connect(**config)

DB_NAME = 'PaisPosiblePython'
cursor = cnx.cursor()
#crear tabla
cursor.execute("CREATE DATABASE PaisPosible_EncuestasHoy")
cursor.execute("")
cursor.close()
cnx.close()