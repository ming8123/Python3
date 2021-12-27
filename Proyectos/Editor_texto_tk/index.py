from tkinter import *
from tkinter import font
from tkinter import filedialog as FileDialog
from io import open
ruta=""
def nuevo():
    global ruta#para que lo reconozca en el label
    mensaje.set("nuevo")
    ruta = ""
    texto.delete(1.0,"end")#para borrar desde primera linea a final
    root.title(ruta+"Mi editor")
def abrir():
    global ruta #hay que definir ante siempre
    mensaje.set("abrir")
    ruta = FileDialog.askopenfilename(
    initialdir=".",
    filetypes=(("Ficheros","*.txt"),),#si usa mac con rtf no funciona bien,y que no se te olvide nunca la coma
    title="Abrir fichero")#Esto es una forma de guarda la ruta de fichero en la que puedes el formato del fichero .txt .

    if ruta != "":
        fichero = open(ruta,"r")
        contenido = fichero.read()#abrir el fichero y guarda en una variable
        texto.delete(1.0,"end")#hay que borrar siempre lo que hay en el texto (es lo que muestra en la parte blanco)
        texto.insert("insert",contenido)#insertamos el contenido en el texto
        fichero.close()#que no se te olvide cerrar si no lo cierra no funciona
        root.title(ruta+"Mi editor")

def guardar():
    global ruta   
    mensaje.set("guardar")
    if ruta != 0:
        contenido=texto.get(1.0,"end-1c")
        fichero =open(ruta,"w+")
        fichero.write(contenido)
        fichero.close() 
        mensaje.set("El fichero se ha guardado correctamente")   
    else:
        guardarcomo()

def guardarcomo():
    global ruta
    mensaje.set("guardar como")
    fichero = FileDialog.asksaveasfile(title="guardar fichero",mode="w",defaultextension=".txt")#guardar el nombre del fichero
    if fichero is not None:
        ruta = fichero.name#este propiedad lo que hace es que guarda la ruta completa del fichero
        contenido=texto.get(1.0,"end-1c")#guarda el contenido del texto ,y el -1c lo que hace es configurar el puntero al ultima caracter
        fichero =open(ruta,"w+")#abrir fichero con la ruta y cargar el antiguo dado de texto con w
        fichero.write(contenido)#guardar nuevo contenido 
        fichero.close() 
        mensaje.set("El fichero se ha guardado correctamente")   
    else:
        mensaje.set("cancerado")
        ruta = ""




#Configurar para raiz
root=Tk()
root.title("Editor")

menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)#menu de la parte superior
filemenu.add_command(label="Nuevo",command=nuevo)
filemenu.add_command(label="Abrir",command=abrir)
filemenu.add_command(label="Guardar",command=guardar)
filemenu.add_command(label="Guardar como",command=guardarcomo)
filemenu.add_separator()
filemenu.add_command(label="Salir",command=root.quit)#cerra afuerza el comand
menubar.add_cascade(menu=filemenu,label="Archivo")#la cabecera del menu

root.config(menu=menubar)#para asignar a root el menubabar
#cuerpo del programa
texto=Text(root)
texto.pack(fill="both",expand=1)
texto.config(bd=12,padx=5,pady=6,font=("Consola",24))
#monitor inferior
mensaje=StringVar()#definir variable
mensaje.set("Este es un editor de texto")#crear texto
monitor=Label(root,textvar=mensaje,justify="left")#crear label y añadir variable
monitor.pack(side="left")


#final para ejecutar
root.mainloop()