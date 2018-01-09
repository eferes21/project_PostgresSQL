
import mysql.connector

con = mysql.connector.connect(user="root", password="",  host="127.0.0.1", database="pythonbd")

cursor =con.cursor()

#query001 ("CREATE TABLE usuario (nombre varchar(100), edad integer , mail  varchar (100))")
query001=" INSERT INTO usuario (nombre, edad, mail) VALUES ('juan', 25 , 'efere @gmail.com')"  
#query001 ="DELETE *FROM usuario WHERE edad=25"
cursor.execute(query001)
"""
rows= cursor.fetchall()
for row in rows:
	print (row)"""



con.commit()
con.close()
