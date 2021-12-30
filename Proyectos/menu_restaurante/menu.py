import sqlite3
from tkinter import *
root = Tk()
root.title("BAR DE MING -MENU")
root.resizable(0,0)
root.config(bd=25,relief="sunken")
Label(root,text='  Bar de ming   ',fg="blue",font=("Times New Roman",28,"bold italic")).pack()
Label(root,text='Menu del dia',fg="red",font=("Times New Roman",22,"bold italic")).pack()
Label(root,text="").pack()
conexion =sqlite3.connect("restaurante.db")
cursor = conexion.cursor()
categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
        print("{}".format(categoria[1]))
        Label(root,text=categoria[1],fg="black",font=("Times New Roman",18,"bold italic")).pack()
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            Label(root,text=plato[1],fg="gray",font=("Verdana",14,"italic")).pack()
  
Label(root,text="Precio sin truco 10 $",fg="green",font=("Times New Roman",18,"bold italic")).pack(side=RIGHT)

conexion.close()
root.mainloop()