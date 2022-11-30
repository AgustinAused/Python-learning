
import mysql.connector 

Database = mysql.connector.connect(
host="localhost", #servidor 
user="root", #user de la conexion de la base de datos     
password="Agustin-aused4", #contraseña de la conexion con la base de datos 
database=" myBaseDeDatos" #conectadose a la base de datos 
)


myBasedeDatos = Database.cursor() 

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
lista = [("John", "Highway 21"),("agus", "estrada 1234"),("jose", "lavalle 1235"),("oliv", "Highway 21"),("juan", "Highway 21"),("maria", "Highway 21"),('martu', "Highway 21"), ("ramona", "Highway 21"),("benja", "Highway 21"),("clau", "Highway 21")]

# myBasedeDatos.executemany(sql,lista) \\ para agregar una lista
for i in lista:
    myBasedeDatos.execute(sql,i)
    print("1 record inserted, ID:", myBasedeDatos.lastrowid)
    Database.commit()
print("record inserted.")


#agregas uno y indicas 
val = ('agustin aused','belgrano 1532')
myBasedeDatos.execute(sql,val)
Database.commit()
print("1 record inserted, ID:", myBasedeDatos.lastrowid)

# leer datos 
myBasedeDatos.execute("select * from customers")
oneResult = myBasedeDatos.fetchone()#devuelve el primer resulado de la tabla 
print('el primer resultado es: ',oneResult)
myresult = myBasedeDatos.fetchall() #
for x in myresult: 
    print(x) #devuelve todas las filas o registros

#filtrar en una consulta(WHERE // DONDE)
COM = "SELECT * FROM customers WHERE ID =21"
myBasedeDatos.execute(COM)# ejecuta la varible con el codigo sql 
myresulta = myBasedeDatos.fetchall() # devuelve los valores arrojasdos por la consuulta 
print('el resultado es: ',myresulta)

# elimina todo lo que hay en la base de datos 
sql = "DELETE FROM customers WHERE id != 0"


print(myBasedeDatos.rowcount, "record(s) deleted")
myBasedeDatos.execute(sql)
Database.commit()
print('delete data Table...')


