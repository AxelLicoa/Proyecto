# Modifique el algoritmo del problema anterior para que, en vez de comprobar que el número sea menor que 10
#  compruebe que se encuentre en el rango (0, 20).

numero = int(input("Ingrese un número:"))
while numero>20 or numero<0:
 numero = int(input("Ingrese un número:"))
print ("número", numero, "correcto")

