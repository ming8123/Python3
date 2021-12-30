import sqlite3
from sqlite3.dbapi2 import OperationalError
def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute('''
                CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)
                
    ''')  
    except sqlite3.OperationalError:
            print("la tabla categoria ya existe")                     
    else:
            print("la tabla categoria ya esta creada")
    
    try: 
        cursor.execute('''          
                CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))
      
    ''')
    except sqlite3.OperationalError:
            print("la tabla plato ya existe")                     
    else:
            print("la tabla plato ya esta creada")




    conexion.close()

def agregar_categoria():
    categoria = input("nombre de la nueva categoria?\n")
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO categoria VALUES(null,'{}')".format(categoria))
    except sqlite3.IntegrityError1:
        print("la categoria con este nombre ya existe")
    else:
        print("todo ok")
    conexion.commit()
    conexion.close()



def agregar_platos():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoria a la plato")
    for categoria in categorias:
        print("[{}]:{}\n".format(categoria[0],categoria[1]))
    
    num = int(input(">>>\n"))
    plato = input("nombre de la nueva plato?\n")

    try:
        cursor.execute("INSERT INTO plato VALUES(null,'{}',{})".format(plato,num))
    except sqlite3.IntegrityError1:
        print("la plato con este nombre ya existe")
    else:
        print("el plato ha creado correctamente")

    
    conexion.commit()
    conexion.close()    
def menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        print("{}".format(categoria[1]))
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            print("{}".format(plato[1]))
  
    conexion.close()  
 
crear_bd()
while True:
    print("Bienvenido al gestor del restaurante")
    opcion = input("Introduce una opcion :\n[1]agregar un menu\n[2]agregar un plato\n[3]Mostrar menu\n[4]Salir\n")
    if opcion == "1":
        agregar_categoria()
    elif opcion == "2":
        agregar_platos()
    elif opcion == "3":
        menu()
    elif opcion == "4":
        print ("buen dia")
        break
    else:
        print("opcion introducido no es correcta")