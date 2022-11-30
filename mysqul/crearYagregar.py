
import mysql.connector 
#conecxion a la base de datos 
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