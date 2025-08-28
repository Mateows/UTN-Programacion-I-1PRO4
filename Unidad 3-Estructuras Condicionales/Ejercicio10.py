# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano. 


lugar_hemiferio = int(input("En que hemiferio se encuentra? (1)Hemiferio Norte, (2)Hemiferio Sur"))
tiempo = input("¿Que día y mes se encuentra? DD/MM")

mes, dia = map(int, tiempo.split("/"))



###En proceso