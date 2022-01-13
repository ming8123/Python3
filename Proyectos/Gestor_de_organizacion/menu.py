import os
import help
import manager
def loop():
    while True:
        #os.system('clear')  # limpiar el terminar
        help.clear()
        print("========================")
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Mostrar cliente     ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Salir               ")
        print("========================")

        option = input("> ")
        help.clear()
        #os.system('clear')  # 'clear' para Linux y OS X

        if option == '1':
            print("Listando los clientes...\n")
            manager.show_all()
        if option == '2':
            print("Mostrando un cliente...\n")
            manager.find()
        if option == '3':
            print("Añadiendo un cliente...\n")
            manager.add()
        if option == '4':
            print("Modificando un cliente...\n")
            if manager.edit():
                print("Cliente modificado correctamente\n")
        if option == '5':
            print("Borrando un cliente...\n")
            manager.delete()
        if option == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")