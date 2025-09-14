# Bingo 
# 1. Generá un cartón 5x5 con números aleatorios entre 1 y 50, sin repetirse. 
# 2. Mostrá el cartón al jugador en forma de matriz. 
# 3. El programa debe sortear números al azar entre 1 y 50, uno por uno. 
# 4. Cada vez que salga un número: 
# o Si está en el cartón, reemplazarlo por un 0. 
# o Si no está, avisar que no aparece. 
# o Mostrar el cartón actualizado después de cada sorteo. 
# 5. El juego termina cuando el cartón completo queda en 0 (¡Bingo!). 


# Desafío extra: Validar cuando haya una línea completa (una fila llena de ceros) y mostrar el 
# mensaje "¡Línea!". 

##### Sugerencias para resolverlo 
# • Usar random.sample(range(1,51), 25) para obtener 25 números únicos y luego 
# acomodarlos en la matriz. 
# • Representar el cartón como una lista anidada de 5x5. 
# • Recorrer la matriz con bucles anidados para marcar los números. 
# • Usar un while que termine cuando todos los valores de la matriz sean 0. 


##Carton bingo auomatico  ##Clase 8-9-2025
import random
carton_bingo = random.sample(range(1,51),25) ##Carton de bingo generado

#Creacion de carton para el usuario
indice = 0
carton_usuario = []
for i in range (5):
    fila = []
    for j in range (5):
        fila.append(carton_bingo[indice]) ##Elige numeros únicos para el carton del usuario y se van agregando en la lista "fila"
        indice += 1
    carton_usuario.append(fila) #Ahora al carton del usuario se le agregan los numeros generados por la fila 

#Eleccion de numeros de la maquina
numeros_maquina = list(range(1,51)) #Genero la lista de 50 numeros
random.shuffle(numeros_maquina) #Mezclo esa lista generada para que se den numeros totalmente aleatorios

#Indice de la maquina para que no explote todo el bucle while
indice_maquina = 0

###Inicializacion del juego
print("¡Bienvenido al Bingo!")
print("Su carton es el siguiente:")
for fila in carton_usuario:
    print(fila)



##La condicion es "mientras el indice de la maquina sea menor a la longitud de los numeros de la maquina y la lista NO un TRUE(todos los numeros tienen que ser 0)"
while indice_maquina < len(numeros_maquina) and not all(all(num == 0 for num in fila) for fila in carton_usuario):
    numero = numeros_maquina[indice_maquina]
    indice_maquina += 1
    print(f"Se sortea el número. . . {numero}")
    encontrado = False

    for i in range(5):
        for j in range(5): #Se recorre la lista de filas & columnas del carton_usuario
            if carton_usuario[i][j] == numero: #En caso de que en las filas & columas se encuentre el numero que eligio la maquina
                carton_usuario[i][j] = 0 #Se reemplaza por un 0
                encontrado = True #y la condicion pasa a ser Verdadero e imprime lo de abajo
                print(f"{numero} Lo tenes!!")
            else:
                pass
    if not encontrado: #Y si la condicion de que el numero de la maquina no coincidio con el del carton_usuario, salta a esta linea donde not encontrado pasa a ser VERDADERO
        print(f"{numero} No lo tenes, L")
    else:
        pass
    for fila in carton_usuario:
        print(fila)
    print("-" * 30 ) #Imprime un salto de linea para que no quede todo acumulado

print("¡BINGO!")
