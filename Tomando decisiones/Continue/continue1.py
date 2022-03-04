# la letra P se llama al continue, lo que hace que se salte el print().
#  Es por ello por lo que no vemos la letra P impresa en pantalla.




cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue
    print(letra)