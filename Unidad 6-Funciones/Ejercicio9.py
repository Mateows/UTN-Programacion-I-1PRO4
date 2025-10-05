# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.

def celcius_a_fahrenheit(celcius):
    grados_fahrenheit = (celcius * 9/5) + 32
    return grados_fahrenheit




celcius = float(input("Ingrese la temperatura en gracds C°: "))
print(f"La temperatura en fahrenheit es de: {celcius_a_fahrenheit(celcius)}F°")