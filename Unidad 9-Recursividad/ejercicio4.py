def decimal_a_binario(n):#función recursiva
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


while True:
    try: #Solicito los usuarios al usuario
        num = int(input("Ingrese un número: "))

        if num < 0:
            print("El numero no puede ser menor a 0")
            continue


        ##Llamo a la función recursiva
        if num == 0:
            print("El número en binario es 0")
        else:
            print(f"El número a binario es: {decimal_a_binario(num)}")
            
    except ValueError:
        print("Intente con un numero entero posiivo")
        continue
    break
