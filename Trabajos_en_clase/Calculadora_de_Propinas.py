# El programa debe: 
# ✓ Pedir al usuario el monto total de la cuenta. 
# ✓ Calcular la propina sugerida al 10%. 
# ✓ Calcular la propina sugerida al 15%. 
# ✓ Calcular el total a pagar en ambos casos (cuenta + propina). 
# ✓ Mostrar todos los resultados en pantalla. 


#Ingreso de datos
monto_total = float(input("¿Cuanto va a pagar? "))
# Cálculo de propinas
propina_sugerida1 = monto_total * 0.10
propina_sugerida2 = monto_total * 0.15
print("Propina sugerida al 10% :$", propina_sugerida1)
print("Propina sugerida al 15% :$", propina_sugerida2)
# Cálculo para el total a pagar
monto_final_propina1 = monto_total + propina_sugerida1
monto_final_propina2 = monto_total + propina_sugerida2
# Mostrar resultados
print("Total a pagar (10%) :$", monto_final_propina1)
print("Total a pagar (15%) :$", monto_final_propina2)