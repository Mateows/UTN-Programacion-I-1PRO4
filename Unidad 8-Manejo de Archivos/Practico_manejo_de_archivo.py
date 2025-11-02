import csv

#Parte 1
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,250.0,15\n")
    archivo.write("Goma,50.0,40\n")

#Parte 2
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre}\n Precio: ${precio}\n Cantidad: {cantidad}\n")

#Parte 3
# Mostrar productos existentes
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre}\n Precio: ${precio}\n Cantidad: {cantidad}\n")

# Pedir nuevo producto
nuevo_nombre = input("Ingrese el nombre del nuevo producto: ")
nuevo_precio = input("Ingrese el precio: ")
nueva_cantidad = input("Ingrese la cantidad: ")

# Agregar al archivo sin borrar lo anterior
with open("productos.txt", "a") as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")


#Parte 4
productos = []
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

# Mostrar la lista de diccionarios
for p in productos:
    print(p)

#Supongamos que ya tenemos la lista "productos" cargada como en la actividad anterior
#Parte 5
buscar_nombre = input("Ingrese el nombre del producto a buscar: ")

encontrado = False
for producto in productos:
    if producto["nombre"].lower() == buscar_nombre.lower():
        print(f"Producto encontrado:\n Nombre: {producto['nombre']}\n Precio: ${producto['precio']}\n Cantidad: {producto['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("Producto no encontrado.")



# Sobrescribir el archivo con los productos actualizados
with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)