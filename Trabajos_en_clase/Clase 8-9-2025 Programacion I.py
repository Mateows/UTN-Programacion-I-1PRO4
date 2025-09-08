##Carton bingo auomatico
import random
carton_bingo = random.sample(range(1,51),25) ##Carton de bingo generado
carton_maquina = random.sample(range(1,51),25)
#Maquina
indice_maquina = 0

#Creacion de carton para el usuario
indice = 0
carton_usuario = []
for i in range (5):
    fila = []
    for j in range (5):
        fila.append(carton_bingo[indice])
        indice += 1
    carton_usuario.append(fila)


###Inicializacion del juego
print("¡Bienvenido al Bingo!")
print("Su carton es el siguiente:")
for fila in carton_usuario:
    print(fila)

####Numero que elige la maquina
for numero in carton_maquina:
    encontrado = False
    print(f"{numero}")


while not all(all(num == 0 for num in fila) for fila in carton_usuario):
    numero = carton_maquina[indice_maquina]
    indice_maquina += 1
    print(f"{numero}")
    encontrado = False
    for i in range(5):
        for j in range(5):
            if carton_usuario[i][j] == numero:
                carton_usuario[i][j] = 0
                encontrado = True
            print(f"El número{numero} se encontro en la posicion [{i},{j}]")
        else:
            print(f"El numero{numero} no se encontro")




