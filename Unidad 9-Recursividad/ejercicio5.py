def es_palindromo(palabra): ##Llamada a la función recursiva
    if len(palabra) <= 1:
        if True:
            return "Sí, es palindromo" #Retorno por verdader
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return "No, no es palindromo" #Retorno por falso




while True:
    try: #Solicito los usuarios al usuario
        letra = (input("Ingrese una palabra: "))

        ##Llamo a la función recursiva
        print(f"¿Es palindromo? -> {es_palindromo(letra)}")
            
    except ValueError:
        print("Intente con un caracter válido")
        continue
    break


