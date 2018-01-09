
import sqlite3

conexion = sqlite3.connect("pydb18.db")

cursor =conexion.cursor()

#cursor.execute("CREATE TABLE usuario (nombre varchar(100), edad integer , mail  varchar (100))")
query001=" INSERT INTO usuario ('nombre', 'edad', 'mail') VALUES ('juan', 25 , 'efere @gmail.com')"  
cursor.execute(query001)


conexion.commit()
conexion.close()
