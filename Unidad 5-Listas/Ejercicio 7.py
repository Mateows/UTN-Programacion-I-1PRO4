#  Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
# cualesquiera. 
autos = ["sedan", "polo", "suran", "gol"]
print(f"Lista sin modificar = {autos}")
##Modifico el contenido de la posicion [1] y [2]
autos[-3] = "mostaza" 
autos[-2] = "mondongo"
print(f"Lista modificada segun el criterio del ejercicio = {autos}")