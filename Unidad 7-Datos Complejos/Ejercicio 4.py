#4 Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe. 

##Funciones para validar los datos ingresados
def validar_clave(clave): #Valido el nombre ingresado, ¿puede ser repetido?, si. ¿Puede contener caracteres especiales y/o números?, no
    while True:
        if not clave.isalpha():
            clave = input("Ingresé un nombre válido (sin caracteres especiales/numeros: ").title()
            continue
        return str(clave)
    
def validar_valor(valor):#Válido el numero ingresado, ¿puede contener caracteres y/o caracteres especiales?, no. ¿Puede ser menor a 6? no
    while True:
        if not valor.isdigit() or len(valor) < 6:
            valor = input("Ingresé un numero telefonico válido de 6 o más caracteres: ")
            continue
        return int(valor)
    

def validar_buscar(buscar): #Válido el nombre ingresado, ¿puede contener caracteres especiales y/o numeros? no
    while True: 
        if not buscar.isalpha():
            buscar = input("Intente un nombre válido: ").title()
            continue
        return str(buscar)

def buscar_contacto(contactos):
    buscar = validar_buscar(input("¿A quien quiere buscar?: ")).title()
    if buscar in contactos:
        print(f"Número de {buscar} +54 9 {contactos[buscar]}")
    else:
        print("Persona no encontrada")


####################################################CODIGO PRINCIPAL######################################################################
contactos  = {}

ITERACION = 1 ##VARIABLE QUE PODES CAMBIAR A CUALQUIER VALOR (Menos negativos no seas asi)
for i in range(ITERACION):
    print(f"Iteracion N°{i+1}")
    while True:
        clave = validar_clave(input("Ingrese clave(nombre): ")).title()
        valor = validar_valor(input("Ingrese el numero(valor) telefonico de 6 o más caracteres: "))
        break
    contactos[clave] = valor


buscar_contacto(contactos) #Llamo la funcion para buscar contactos, definida en la linea 27

