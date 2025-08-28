# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano. 
# Enero 1
# Febrero 2
# Marzo 3
# Abril 4 
# Mayo 5
# Junio 6
# Julio 7 
# Agosto 8 
# Septiembre 9
# Octubre 10
# Noviembre 11
# Diciembre 12
ESTACION = " "



lugar_hemiferio = int(input("En que hemiferio se encuentra? (1)Hemiferio Norte, (2)Hemiferio Sur "))
if lugar_hemiferio == 1 or lugar_hemiferio== 2:
    pass
else:
    print("Hemiferio inexistente, finalizando")
    exit()

tiempo = input("¿Que día y mes se encuentra? DD/MM ")
dia, mes = map(int, tiempo.split("/"))

if lugar_hemiferio == 1: #El condicional entra al Hemiferio Norte en caso de ser 1
    if (mes == 12 and dia >= 21) or (mes in range (1,3)) or (mes == 3 and dia <= 20):
        ESTACION = "Invierno"
    elif mes == 3 and dia >= 21 or mes in range (3,6) or (mes == 6 and dia <=20):
        ESTACION = "Primavera"
    elif mes == 6 and dia >= 21 or mes in range (6,9) or (mes == 9 and dia <=20):
        ESTACION = "Verano"
    elif mes == 9 and dia >= 21 or mes in range (9,12) or (mes == 12 and dia <=20):
        ESTACION = "Otoño"
else:
    if (mes == 12 and dia >= 21) or (mes in range (1,3)) or (mes == 3 and dia <= 20):
        ESTACION = "Verano"
    elif mes == 3 and dia >= 21 or mes in range (3,6) or (mes == 6 and dia <=20):
        ESTACION = "Otoño"
    elif mes == 6 and dia >= 21 or mes in range (6,9) or (mes == 9 and dia <=20):
        ESTACION = "Invierno"
    elif mes == 9 and dia >= 21 or mes in range (9,12) or (mes == 12 and dia <=20):
        ESTACION = "Primavera"


print("Estamos en ", ESTACION)



