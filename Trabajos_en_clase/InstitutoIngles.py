entrada_datos = input("Día de la semana, DD/MM: ")
#Proceso de datos
dia_semana, dato_dia = entrada_datos.split() #Separo en 3 variables distintas el dia, nombre del dia y mes
nombre_del_dia = dia_semana.capitalize() #La primera letra se pondra en mayuscula, independientemente de como se ingrese
fecha, numero_mes = map(int, dato_dia.split("/")) ##Los valores que estaban como un String pasaron a ser enteros, para no generar errores

estudiante= {
    "estudiante_inicial": "Lunes",
    "estudiante_intermedio": "Martes",
    "estudiante_avanzado": "Miercoles",
    "practica_hablada": "Jueves",
    "estudiante_viajero": "Viernes"
}

banderas = {
    "si" : True,
    "no" : False
}
#Variables de examenes#
alumnos_aprobados = 0
alumnos_desaprobados = 0
porcentaje_aprobados = 0
#Variables para practica hablada#
alumnos_presentes = 0
alumnos_ausentes = 0
porcentaje_mayoria = 0
#Alumnos del nuevo ciclo#
alumnos_ciclo_nuevo = 0
alumno_arancel = 0
ingresos_totales = 0


if fecha > 31 or numero_mes > 12:
    print("Error: Fecha o mes inválido.")
elif nombre_del_dia == estudiante["estudiante_inicial"] or nombre_del_dia == estudiante["estudiante_intermedio"] or nombre_del_dia == estudiante["estudiante_avanzado"]: ##En caso de que coincidan con los dias de examenes
    input("¿Se tomaron examenes?")
    if banderas["si"]:
        alumnos_aprobados=int(input("Cuantos alumnos aprobaron")) ##Preguntamos cuantos alumnos aprobaron y cuantos desaprobaron
        alumnos_desaprobados=int(input("Cuantos alumnos desaprobaron"))
        porcentaje_aprobados = (alumnos_aprobados + alumnos_desaprobados) / 100 ##Calculamos el porcentaje de aprobados
        #Salida
        print("El porcentaje de aprobados fue del ", porcentaje_aprobados, "%")
elif nombre_del_dia == estudiante["practica_hablada"]: ##En caso de que el dia sea jueves
    alumnos_presentes=int(input("¿Cuantos alumnos asistieron a la clase?"))
    alumnos_ausentes=int(input("¿Cuantos alumnos faltaron a la clase?"))
    porcentaje_mayoria = (alumnos_presentes + alumnos_ausentes) / 100 ##Sacamos el porcentaje de los alumnos
    #Salida
    if porcentaje_mayoria > 50:
        print("Asistio la mayoria de los alumnos")
    else:
        print("No asistio la mayoria de alumnos")
elif nombre_del_dia == estudiante["estudiante_viajero"] and fecha == 1 and numero_mes == 1 or numero_mes == 7:
    print("Comienzo del nuevo ciclo")  
    alumnos_ciclo_nuevo=int(input("Ingrese la cantidad de alumnos del nuevo ciclo"))
    alumno_arancel=int(input("Ingrese el aracenl en $ de cada alumno"))
    ingresos_totales = alumnos_ciclo_nuevo * alumno_arancel ##Calculamos los ingresos totales
    #Salida
    print("Los ingresos totales del nuevo ciclo son de $", ingresos_totales)
else:
    print("No hay actividades programadas para este día.")     






