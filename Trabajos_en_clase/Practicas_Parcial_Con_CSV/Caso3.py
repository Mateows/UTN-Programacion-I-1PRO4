import csv
import os

def inicializar_archivo():
    if not os.path.exists("farmacia.csv"):
        with open("farmacia.csv", "w", newline="", encoding="utf-8")as archivo:
            escritor=csv.DictWriter(archivo, fieldnames=["nombre", "cantidad"])
            escritor.writeheader()

def cargar_archivo():
    try:
        lista = []
        with open("farmacia.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, fieldnames=["nombre", "cantidad"])
            next(lector)
            for fila in lector:
                try:
                    fila["cantidad"] = int(fila["cantidad"])
                    lista.append(fila)
                except ValueError:
                    print(f"Saltado fila {fila} no pudieron cargarse los datos")
        return lista
    except FileExistsError:
        print("No se encontro el archivo")


def actualizar_archivo(lista):
    with open("farmacia.csv", "w", newline="", encoding="utf-8")as archivo:
        escritor=csv.DictWriter(archivo, fieldnames=["nombre", "cantidad"])
        escritor.writeheader()
        escritor.writerows(lista)
        print("Archivo Actualizado")












def menu():
    print("1. Cargar medicamentos")
    print("2. Mostrar medicamentos")
    print("3. Modificar cantidad de medicamento")
    print("4. Eliminar medicamento")
    print("5. Consultar existencias")
    print("6. Mostrar sin stock")
    print("7. Vender/Comprar medicamentos")
    print("8. Salir ")



def cargar_medicamentos(lista):
        try:
            cant=int(input("Ingrese la cantidad de medicamentos: "))
        except ValueError:
            print("Numero invalido volviendo al menú")
            return


        for agregar in range(cant):
            while True:
                n_medi = input(f"Ingrese el nombre del medicamento N°{agregar+1}: ").capitalize().strip()
                if not n_medi.isalpha():
                    print("Ingrese un nombre valido")
                    continue


                while True:
                    c_medi = input(f"Ingrese la cantidad de unidades para {n_medi}: ")
                    if not c_medi.isdigit():
                        print("Intente con un numero positivo")
                        continue
                    else:
                        c_medi = int(c_medi)
                        lista.append({"nombre":n_medi, "cantidad":c_medi})
                        break
                break
        actualizar_archivo(lista)
        return lista

def consultar(lista):
    while True:
        buscar = input("Ingrese el nombre del medicamento para buscar: ").capitalize()
        if not buscar.isalpha():
            print("Intente con un caracter válido")

        for elem in lista:
            if(buscar == elem["nombre"]):
                print(f"Nombre {elem["nombre"]}- Cantidad: {elem["cantidad"]}")
                return








def mostrar(inventario):
    if not inventario:
        print("No hay nada cargado")
    else:
        for elem in inventario:
            print(f"Nombre {elem["nombre"]}- Cantidad: {elem["cantidad"]}")

def mostrar_sin_stock(inventario):
    if not inventario:
        print("No hay nada cargado")
    else:
        for elem in inventario:
            if(elem["cantidad"] == 0):
                print(f"Nombre {elem["nombre"]}- Cantidad: {elem["cantidad"]}")



def modificar(lista):
    if not lista:
        print("No hay nada cargado")
        return
    
    while True:
        buscar = input("Ingrese el nombre del medicamento para modificar: ").capitalize()
        if not buscar.isalpha():
            print("Intente un caracter")
            continue

        for elem in lista:
            if(buscar == elem["nombre"]):
                try:
                    nuevo_stock = input("Cuanto es el nuevo stock del medicamento: ")
                    elem["cantidad"] = nuevo_stock
                    actualizar_archivo(lista)
                    return lista
                except ValueError:
                    print("Numero invalido")

def eliminar(lista):
    if not lista:
        print("No hay nada cargado")
        return
    

    lista_nva = []
    if not lista:
        print("No hay nada cargado")
        return
    
    while True:
        buscar = input("Ingrese el nombre del medicamento para borrar: ").capitalize()
        if not buscar.isalpha():
            print("Intente un caracter")
            continue

        for elem in lista:
            if(buscar == elem["nombre"]):
                continue
            lista_nva.append(elem)

        actualizar_archivo(lista_nva)
        return lista_nva
    
    
def compra_venta(lista):
    if not lista:
        print("No hay nada cargado")
        return
    
    
    while True:
        buscar = input("Ingrese el medicamento a buscar: ").capitalize()
        if not buscar.isalpha():
            print("Caracter invalido, intente de nuevo")
            continue
        for elem in lista:
            if(buscar == elem["nombre"]):
                opc = int(input("Ingrese una opcion: (1. Vender) (2. Comprar): "))
                match opc:
                    case 1:
                        for elem in lista:
                            if(elem["cantidad"]== 0):
                                print("No hay productos que vender")
                            else:
                                try:
                                    cant_vender = int(input("Ingrese la cantidad de productos a vender: "))
                                    if(elem["cantidad"] < cant_vender):
                                        print("No puede vender mas productos de los que contamos")
                                    else:
                                        elem["cantidad"] -= cant_vender
                                        actualizar_archivo(lista)
                                        return lista
                                except ValueError:
                                    print("Son numeros enteros, intente con uno")
                    case 2:
                        try:
                            cant_comprar = int(input("Ingrese la cantidad de productos a comprar: "))
                            elem["cantidad"] += cant_comprar
                            actualizar_archivo(lista)
                            return lista
                        except ValueError:
                            print("Son numeros enteros, intente con uno")
                    case _:
                        print("Opcion invalida, volviendo al menu")
                        return lista

def programa_principal():
    inicializar_archivo()
    inventario = cargar_archivo()
    while True:
        try:
            menu()
            opc = int(input("Ingrese una opcion"))
            match opc:
                case 1: #Cargar
                    inventario = cargar_medicamentos(inventario)
                case 2: #Mostrar
                    mostrar(inventario)
                case 3: #Modificar
                    inventario = modificar(inventario)
                case 4: #Eliminar
                    inventario = eliminar(inventario)
                case 5: #Consultar
                    inventario =  consultar(inventario)
                case 6: #Listar
                    mostrar_sin_stock(inventario)
                case 7: #Comprar/Vender
                    inventario = compra_venta(inventario)
                case 8:
                    print("Adios")
                    break
                case _:
                    print("Ingrese un numero dentro del rango (1-8)")
        except ValueError:
            print("Numero Invalido")



if __name__ == "__main__":
    programa_principal()