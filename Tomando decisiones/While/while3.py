# Modifique el algoritmo del problema anterior para que cuente las veces que ha leído un número de teclado y 
# escriba el resultado por pantalla.

contador = 1
numero = int(input("Ingrese un número"))
while numero>20 or numero<0:
 numero = int(input("Ingrese un número"))
 contador += 1
print ("Número ingresado:",numero)
print ("Número de intentos:",contador)