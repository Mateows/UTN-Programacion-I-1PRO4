def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



while True:
    try:
        num = int(input("Ingrese un número: "))
        if num < 0:
            print("Ingrese un numero mayor a 0")
            continue
        print("Serie fibonacci")
        for i in range(num):
            print(fibonacci(i))
            
    except ValueError:
        print("Intente con un numero entero posiivo")
        continue
    break





