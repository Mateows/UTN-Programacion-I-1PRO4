#Ejercicio Extra que implemente de uno de los ejercicios del Pre-Universitario 
def invertir_cadena(texto):#Función recursiva
    if len(texto) <= 1:
        return texto
    else:
        return invertir_cadena(texto[1:]) + texto[0]




while True:
    try: #Solicito los usuarios al usuario
        letra = (input("Ingrese una palabra: "))
        if not letra.isalpha():
            print("Ingrese un caracter (no permito números muajaja)")
            continue
        

        ##Llamo a la función recursiva
        print(f"Letra {letra} invertida -> {invertir_cadena(letra)}")
            
    except ValueError:
        print("Intente con un caracter válido")
        continue
    break