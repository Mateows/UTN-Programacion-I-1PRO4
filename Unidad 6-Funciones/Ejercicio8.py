# Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales

def calcular_imc(peso, altura):
    IMC = peso / (altura*altura)
    return IMC


peso = float(input("Ingresé su peso: "))
altura = float(input("Ingresé su altura: "))
print(f"Su IMC es: {calcular_imc(peso,altura)}")