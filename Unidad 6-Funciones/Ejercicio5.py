# Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

def validar_segundos(): #Valido los segundos que no sean flotantes/caracteres especiales/caracteres y/o números negativos
    while True:
        segundos = input("Ingrese los segundos a convertir")
        if segundos.isdigit():
            segundos = int(segundos)
            return segundos
        else:
            print("Ingrese el tiempo(segundos) positivo")
            continue


def segundos_a_horas(segundos): 
    hora = segundos//3600
    return hora

segundos = validar_segundos()
print(f"Los segundos convertidos a horas son: {segundos_a_horas(segundos)}")
