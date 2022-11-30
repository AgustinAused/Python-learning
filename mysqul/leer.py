import mysql.connector 

Database = mysql.connector.connect(
host="localhost", #servidor 
user="root", #user de la conexion de la base de datos     
password="Agustin-aused4", #contraseña de la conexion con la base de datos 
database=" myBaseDeDatos" #conectadose a la base de datos 
)

myBasedeDatos = Database.cursor() 
# leer datos 
myBasedeDatos.execute("select * from customers")
oneResult = myBasedeDatos.fetchone()#devuelve el primer resulado de la tabla 
print('el primer resultado es: ',oneResult)
myresult = myBasedeDatos.fetchall() #
for x in myresult: 
    print(x) #devuelve todas las filas o registros


# seleccionar con un filtro 
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

myBasedeDatos.execute(sql)

myresult = myBasedeDatos.fetchall()

for x in myresult:
    print(x)