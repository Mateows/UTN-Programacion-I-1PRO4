# Crear una función llamada informacion_personal(nombre, apellido,
#  edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#  [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados. 

def pedir_nombre(): #Valido el nombre del usuario
    while True:
        nombre = input("Ingrese su nombre: ")
        if nombre.isalpha(): #Si el nombre esta ingresado correctamente "mAteO", retornara el nombre de "Mateo" y saldra del bucle while volviendo al programa principal
            return nombre.capitalize()
        else: #Seguira en un bucle indefinido hasta que se ingresen correctamente los datos
            print("Ingrese un nombre válido (sin caracteres especiales(@-$-&) y/o números (123))")
            continue

def pedir_apellido(): #Valido el apellido del usuario
    while True:
        apellido = input("Ingrese su apellido: ")#Lo mismo que en nombre, si se ingresa "consollo" retornara "Consollo" y saldra del bucle while volviendo al programa principal
        if apellido.isalpha():
            return apellido.capitalize()
        else: #Seguira en un bucle indefinido hasta que se ingresen correctamente los datos
            print("Ingrese un nombre válido (sin caracteres especiales(@-$-&) y/o números (123))")
            continue

def pedir_edad(): #Valido la edad del usuario
    while True:
        edad = input("Ingrese su edad: ")#Si es correcta la entrada, retornara un valor ENTERO al programa principal
        if edad.isdigit():
            edad = int(edad)
            return edad
        else: #Seguira en un bucle indefinido hasta que se ingresen correctamente los datos
            print("Ingresé una edad válidad (sin caracteres especiales(@-%-&) y/o letras (a-z))")
            continue

def pedir_residencia(): #Valido la ubicación geográfica del usuario(obviamente puede ser, no sé Micasa, y va a tomarlo como válido)
    while True:
        residencia = input("Ubicacion geográfica: ") #Si se ingresa "micasita" retornara "Micasita" y saldra del bucle while volviendo al programa principal
        if residencia.isalpha(): 
            return residencia.capitalize() #Retorna la variable capitalizada y sale del while, ej; argentina -> retorna "Argentina"
        else: #Seguira en un bucle indefinido hasta que se ingresen correctamente los datos
            print("Ingrese una ubicacion geografica válida (sin caracteres especiales(@-$-&) y/o números)")
            continue
#presentacion(el enunciado del ejercicio)
def informacion_personal(nombre,apellido,edad,residencia):
    presentacion = f"Hola! Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}, un gusto conocerte"
    return presentacion




#Programa principal
nombre = pedir_nombre()
apellido = pedir_apellido()
edad = pedir_edad()
residencia = pedir_residencia()
print(informacion_personal(nombre,apellido,edad,residencia))