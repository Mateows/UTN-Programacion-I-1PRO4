# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe. 
def consultar_producto():
    producto = "Que producto desea buscar? :".lower().strip()
    if producto not in stock_verduleria:
        print("El producto no se encontro")
    else:
        print(f"Hay {stock_verduleria[producto]} unidades de {producto}")
        return print()



def agregar_stock():
    producto = input("Ingrese el producto al que desee agregarle más stock: ").capitalize().strip()
    if producto not in stock_verduleria:
        print("El producto no se encontro")
    else:
        try:
            cantidad = int(input("¿Cuantas unidades desea agregar?:" ))
            stock_verduleria[producto] += cantidad
            print(f"Se agregaron {cantidad} unidades nuevas de {stock_verduleria[producto]}.")
            return print()
        except ValueError:
            print("Ingrese un numero valido")

def agregar_nuevo_producto():
    nuevo_producto = input("Ingrese el nombre del nuevo producto: ").lower().strip()
    if not nuevo_producto.isalpha():
        print("Caracter inválido")
        return print()

    nuevo_producto = str(nuevo_producto)

    if nuevo_producto in stock_verduleria:
            print("Ese producto ya existe")
    else:
        try:
            cantidad = input("Ingrese la cantidad que desea agregar: ")
            stock_verduleria[nuevo_producto] = cantidad
            print(f"El producto {nuevo_producto} se agrego con {cantidad} unidades")
            return print()
        except ValueError:
            print("Ingrese un numero válido")


stock_verduleria = {"manzanas": 15,
                    "peras": 24,
                    "bananas": 33,
                    "kiwis": 11
                    }


while True:
    print("---MENÚ---")
    print("1. Consultar Stock")
    print("2. Agregar unidades al stock")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    opcion = input("Ingrese una opcion: ")
    match opcion:
        case "1":

            producto = consultar_producto()
        case "2":
            if not stock_verduleria:
                print("No hay productos cargados")
                continue

            stock_producto = agregar_stock()
        case "3":
            producto_nuevo = agregar_nuevo_producto()
        case "4":
            print("Adiós")
            break
        case _:
            print("Intente una opcion valida")

print(stock_verduleria)