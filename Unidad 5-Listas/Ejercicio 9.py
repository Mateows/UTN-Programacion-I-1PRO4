# Dada la lista “compras”, cuyos elementos representan los productos comprados por 
# diferentes clientes: 

# a)Agregar "jugo" a la lista del tercer cliente usando append. 
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
# c) Eliminar "pan" de la lista del primer cliente.  
# d) Imprimir la lista resultante por pantalla 



compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print(f"Lista sin modificaciones = {compras}")
#Modifico el vector [2], modifico contenido del vector [1] en la posicion [1], y borro el contenido del vector [0]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(f"Lista modificada segun el criterio del ejercicio = {compras}")


