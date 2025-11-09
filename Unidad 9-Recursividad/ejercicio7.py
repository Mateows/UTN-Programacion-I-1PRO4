def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)











while True:
    try: #Solicito los usuarios al usuario
        num = int(input("Ingrese el número de bloques en el nivel mas bajo: "))
        if num < 0:
            print("Ingrese un numero entero positivo")
            continue

        ##Llamo a la función recursiva
        print(f"Total de bloques faltantes para construir la piramide: {contar_bloques(num)}")
    except ValueError:
        print("Intente con un número valido válido")
        continue
    break
