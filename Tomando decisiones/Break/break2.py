#Ejecutando break
# La condición while True haría que la sección de código se ejecutara indefinidamente
#  pero al hacer uso del break, el bucle se romperá cuando x valga cero.
x = 5

while True:
    x -= 1
    print(x)
    if x == 0:
        break
    print("Fin del bucle")