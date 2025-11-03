import os
import csv



def inicializar_archivo():
    if not os.path.exists("almacen.csv"):
        with open("almacen.csv", "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "cantidad"])
            escritor.writeheader()


def cargar_archivo():
    try:
        lista = []
        with open("almacen.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, fieldnames=["nombre", "cantidad"])
            next(lector)
            for fila in lector:
                try:
                    fila["cantidad"] = int(fila["cantidad"])
                    lista.append(fila)
                except ValueError:
                    print("Saltando linea")
        return lista
    except FileExistsError:
        print("ERROR. Archivo no encontrado")


def actualizar_archivo(lista):
    with open("almacen.csv", "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "cantidad"])
        escritor.writeheader()
        escritor.writerows(lista)
        print("Lista Actualizada")

######################################
def menu():
    print("1. Cargar prendas")
    print("2. Mostrar prendas")
    print("3. Modificar stock")
    print("4. Eliminar prenda")
    print("5. Consultar stock por nombre")
    print("6. Listar sin stock")
    print("7. Vender/Comprar")
    print("8. Salir")



def cargar_productos(lista):
            try:
                cant_i = int(input("Ingrese la cantidad de prendas: "))
            except ValueError:
                print("Dato invalido, volviendo al menu")
                return
            
            for i in range(cant_i):
                while True:
                    n_ropa = input(f"Ingrese el nombre de la prenda:{i+1} ").capitalize()
                    if not n_ropa.isalpha():
                        print("Ingrese una letra")
                        continue

                    while True:
                        c_ropa = input("Ingrese la cantidad de stock: ")
                        if not c_ropa.isdigit():
                            print("Ingrese un numero")
                            continue
                        else:
                            lista.append({"nombre":n_ropa, "cantidad":c_ropa})
                            break
                    break
            actualizar_archivo(lista)
            return lista

def mostrar_todo(lista):
    for elem in lista:
        print(f"Nombre: {elem["nombre"]} - Stock: {elem["cantidad"]}")


def modificar_prenda(lista):
    while True:
        buscar = input("Ingrese el nombre de la prenda para buscar: ").capitalize()
        if not buscar.isalpha():
            print("Intente con una letra")
            continue
        for elem in lista:
            if(buscar == elem["nombre"]):
                try:
                    modificar = int(input("Ingrese la nueva cantidad de stock: "))
                    elem["cantidad"] = modificar
                    actualizar_archivo(lista)
                    return lista
                except ValueError:
                    print("Intente con un numero")





def mostrar_sin_stock(lista):
    for elem in lista:
        if(elem["cantidad"]==0):
            print(f"Nombre: {elem["nombre"]} - Stock: {elem["cantidad"]}")

def eliminar_prenda(lista):
    lista_nva = []
    buscar = input("Ingrese el nombre de la prenda a borrar: ").capitalize()
    if not buscar.isalpha():
        print("Nombre invalido, volviendo al menu")
        return
    else:
        for elem in lista:
            if(buscar == elem["nombre"]):
                continue
            lista_nva.append(elem)
        actualizar_archivo(lista_nva)
        return lista_nva


def consultar(lista):
    buscar = input("Ingrese el nombre de la prenda para consultar: ").capitalize()
    if not buscar.isalpha():
        print("Nombre invalido volviendo al menú")
    else:
        for elem in lista:
            if(buscar == elem["nombre"]):
                print(f"Nombre: {elem["nombre"]} - Stock: {elem["cantidad"]}")            



def venta_compra(lista):
    while True:
        buscar = input("Ingrese la prenda a buscar: ").capitalize()
        if not buscar.isalpha():
            print("Intente con una letra")
            continue

        for elem in lista:
            if(buscar == elem["nombre"]):
                opc=int(input("Ingrese una opcion (1-Vender) (2-Comprar): "))
                match opc:
                    case 1:
                        if(elem["cantidad"]== 0):
                            print("No hay unidades disponibles")
                        else:
                            try:
                                cant = int(input("Ingrese la cantidad de prendas para vender: "))
                                if(elem["cantidad"] < cant):
                                    print("El numero supera a la cantidad disponible")
                                else:
                                    elem["cantidad"] -= cant
                                    print("Unidades vendidas")
                                    actualizar_archivo(lista)
                                    return lista
                            except ValueError:
                                print("Numero negativo.")
                    case 2:
                        if(elem["cantidad"]== 0):
                            print("No hay unidades disponibles")
                        else:
                            try:
                                cant = int(input("Ingrese la cantidad de prendas para comprar: "))
                                elem["cantidad"] += cant
                                print("Unidades compradas")
                                actualizar_archivo(lista)
                                return lista
                            except ValueError:
                                print("Numero negativo.")






def programa_principal():
    inicializar_archivo()
    inventario = cargar_archivo()
    while True:
        try:
            menu()
            opc =int(input("Ingrese una opción: "))
            match opc:
                case 1: #Cargar
                    inventario = cargar_productos(inventario)
                case 2: #Mostrar
                    mostrar_todo(inventario)
                case 3: #Modificar
                    inventario = modificar_prenda(inventario)
                case 4: #Eliminar
                    inventario = eliminar_prenda(inventario)
                case 5: #Consultar stock
                    inventario = consultar(inventario)
                case 6: #Listar sin stock
                    mostrar_sin_stock(inventario)
                case 7: #Comprar/vender
                    inventario = venta_compra(inventario)
                case 8:
                    print("ADIOS")
                    break
                case _:
                    print("Intente con un número dentro de las opciones (1-8)")
        except ValueError:
            print("Valor invalido, intente con otro")




if __name__ == "__main__":
    programa_principal()
