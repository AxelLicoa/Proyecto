#la x vale 3, se llama al continue, lo que hace que se salte el resto de código de la iteración (el print()). 
# Por ello, vemos como el número 3 no se imprime en pantalla.


x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)