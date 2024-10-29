import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="usuarios"
)

# Verificación de conexión
if database.is_connected():
    print("Conexión exitosa a la base de datos")
else:
    print("Error en la conexión a la base de datos")
