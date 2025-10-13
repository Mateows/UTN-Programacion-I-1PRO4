#9)Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
#permitir consultar que actividad hay en cierto dia y hora


agenda_diaria = {
                ("Lunes", "8:00 A.M. hasta las 1:00 P.M."): "Programación",
                ("Martes", "9:00 A.M hasta las 2:00 P.M."): "Mátematicas",
                ("Miercoles", "7:14 A.M hasta las 10:30 A.M."): "Organización Empresarial",
                ("Jueves", "8:00 A.M. hasta las 12:30 P.M."): "Meet Virtual de Programación",
                ("Viernes", "12:30 P.M. hasta las 3:14 P.M."): "Arquitectura en Sistemas Operativos",
                ("Sabado", "15:15 P.M. hasta las 20:15 P.M."): "Estudiar",
                ("Domingo", "Libre todo el día"): "Descansar"
                }
encontrado = False

consulta_agenda = input("Qué dia desea consultar: ").capitalize().strip()

for (dia, horario), materia in agenda_diaria.items():
    if dia == consulta_agenda:
        print(f"El día {dia}, tenes {materia} desde las {horario}")
        encontrado = True
        break

if not encontrado:
        print("Dia no encontrado")