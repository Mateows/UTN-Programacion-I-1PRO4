# Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    radio = 3.14159 * radio**2
    area = radio
    return area

def calcular_perimetro_circulo(radio):
    radio = 2 * 3.14159 * radio
    perimetro = radio
    return perimetro


radio = float(input("Ingrese el radio del circulo: "))
print(f"El área del circulo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del circulo es: {calcular_perimetro_circulo(radio)}")
