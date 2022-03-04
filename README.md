## ¿Qué es Python?![imagen](https://user-images.githubusercontent.com/99735479/156707792-1f4405ab-475c-4f8b-af3b-f71414e0b513.png)
Python, es uno de los muchos lenguajes de progrmación que existe. Lo que hace diferente a python es que tiene un lenguaje interpretado, no hay necesidad de compilarlo para que se lleve acabo las acciones que defines en python, si no que estás se ejecutan directamente por el ordenador.
## ¿Qué es una variable?
Las variables en python pueden estar representadas normalmente por letras, nombres, pronombres, etc... Es donde guardamos los datos ya sea de tipo, str, int o float.
### Nombrando una variable

  Creo una variable de nombre dia
 ```python
  dia = "Lunes" 
  ```
  Imprimo el tipo de variable
  
  ```python
  print(type(dia))
  dia = 21
  print(dia)
  ```
  Para sabe el tipo de variable utilizamos la función type
  ```python
  print(type(dia))
  dia = 21.5
  print(type(dia))
  ```


### Asignando valores a una variable

Asignaciones en la misma linea
``` python
x=12; y=10; z=4
print('x', x)
print('y', y)
print(z)
print('x=', x, 'y=', y, 'z=', z)
```
Asignación multiple
``` python
dia, mes, anho = "Martes", "Diciembre", 2021
print(dia,mes,anho)
print('Hoy es', dia)
print(', el mes actual es', mes)
print('y el año es', anho)
print('Hoy es', dia, ', el mes actual es', mes, 'y el año es', anho)
``` 
Asignación del mismo valor
``` python
var1 = var2= 10
```
Asignación de intercambio
``` python
base=10; altura=100
base, altura = altura, base
print('base', base)
print('altura', altura)
```

## Operadores básicos

### Suma
Es una de las operaciones matemáticas en la que se necesita de dos o más números para poder efectuarse. Le podemos asignar variables a estos números y sumarlas.
``` python
num1 = 12
num2 = 13

suma = num1 + num2
print(num1, '+', num2, '=',suma)
``` 
### Resta
Operación matemática en la que se necesita de dos o más números para poder efectuarse. Le podemos asignar variables a estos números y restarlas.
``` python
num1 = 89
num2 = 20

resta = num1 - num2
print(num1, '-', num2, '=',resta)
``` 
### Multiplicación

En esta operación el orden de los factores no alera el producto. Le podemos asignar variables a estos números y multiplicarlas.
``` python
multiplicacion = num1 * num2
print(num1, 'x', num2, '=',multiplicacion)
Y como el orden de los factores no altera al producto podemos hacerlo de la siguiente forma 
multiplicacion = num2 * num1
print(num2, 'x', num1, '=',multiplicacion)
``` 

### División

Aquí hay que tener mucho cuidado, no podemos dividir para cero así que no podemos darle 0 a una variable y el orden de los factores si altera al producto. Asignaremos variables y procedemos a efectuar la operación.
``` python
num1= 50
num2= 5
division = num1 / num2
print(num1, '/', num2, '=',division)
```
### Módulo

Operador aritmético que nos sirve para poder obtener el residuo de las divisiones.
``` python
num1= 80
num2= 7

mod = num1 % num2
print(num1, '%', num2, '=',mod)
```


## Tipos de datos en Python

### Integer

Utilizamos integer que en lenguaje python se escribe "int" cuando nos referimos a números enteros, ya sean positivos o negativos. Un claro ejemplo de esto es la edad de una persona.
``` python

edad= int(input("Ingrese la edad de la persona: "))

print(edad, "años")
``` 

### Float

Float, nos indica los números negativos o positivos con uno o más decimales. Por lo general lo encontramos más en promedios.
``` python
promedio= 8.6

print(type(promedio))
```
### String

String en python, se lo representa cuando está entre comillas, ya sea una comilla: 'Hola mundo'; y doble comillas: "Hola mundo".

asignando varibales str de dos modos
``` python

name1= 'Ismael'
name2= "Genesis"

print(name1,"Y", name2)
print(type(name1 and name2))

```


## Casting en Python
### Cast

Realizar un cast o casting, significa cambiar un tipo de dato a otro, ya sea este, str, int o float.
``` python
  a= "15"
  print(type(a))
  *este imprimirá que es de clase <<str>>*
  ahora lo cambiaremos a int
  a= int(a)
  print(type(a))
  *aquí imprimirá el cambio de dato, ahora será <<int>>*
  ```
### List

Las listas se utilizan para almacenar varios datos en una sola variable.
``` python

Materias =["Química", "Matemáticas", "Lenguaje", "Física"]
print(Materias)
```
### Tuple

Las  tuplas se utilizan para almacenar varios elementos ya sean homogéneos y heterogéneos, normalmente se los separa con una coma, tiene una semenjanza con la "list" con la diferencia que son inmutables.
``` python
número= (10, 5, 8, 14)
print(número)
```
Si yo quiero saber cuántos elementos tiene mi tupla coloco:
``` python
print(len(número))
``` 
### Dictionary
Estos diccionarios se utilizan para almacenar valores de datos en pares "clave: dato"
``` python
Carro = {
  "carro": "Ford",
  "modelo": "Mustang",
  "anho": 1964
}
print(Carro)
``` 

## Tomando decisiones
### Sentencia if
La estructura de control "if" permite que un programa ejecute unas instrucciones cuando se cumplan una condición. En inglés "if" significa "si" (condición).
#### Elif
La palabra clave elif es la forma de Python de decir "si las condiciones anteriores no fueron ciertas, intente esta condición".
#### Else
La palabra clave else captura cualquier cosa que no esté capturada por las condiciones anteriores.

Escribir un programa que solicite un valor entero al usuario y 
determine si es positivo o negativo.
``` python
num = int(input("Ingrese numero: "))

if num == 0:
    print('cero')
elif num > 0:
    print('positivo')
else:
    print('negativo')
 ```

### Ciclo For
Un bucle for se usa sobre una secuencia (es decir, una lista, una tupla, un diccionario, un conjunto o una cadena).Con el bucle for podemos ejecutar un conjunto de sentencias, una vez por cada elemento de una lista, tupla, conjunto, etc.
Calcular la suma y la media aritmetica de Nnumeros reales. 
solicitar el valor de n al usuario y cada uno de los N números reales.
``` python
n = int(input("Ingrese los números que desee: "))
suma= 0
for i in range(n):
    nota =int(input('Ingrese el número' + str (i+1) +  ':'))
    suma += nota
    
promedio = suma/n 
print("promedio:", promedio)
print(type(promedio))
```
### Ciclo While
Con el bucle while podemos ejecutar un conjunto de declaraciones siempre que una condición sea verdadera.
Realizar un menú que indique la operación que desea realizar y efectuarla.
``` python
op=1
num1=0
num2=0
while op !=0:

    print ("<1> Sumar")
    print ("<2> Restar")
    print ("<3> Multiplicar")
    print ("<4> Dividir")
    print ("<0> Salir")

    op=int(input("Ingrese opción:"))

    if op !=0:
        num1=int(input("ingrese num1:"))
        num2=int(input("ingrese num2:"))

    if op==1:
        print("Suma:", num1+num2)
    elif op==2:
        print("Resta:", num1-num2)
    elif op==3:
        print("Multiplicación:", num1*num2)
    elif op==4:
        print("División:", num1/num2)

    else:
        print("No existe esa opción")
  ```
### Break
Con la instrucción break podemos detener el bucle incluso si la condición while es verdadera:
``` python
contador = 0
for i in range(10):
    for j in range (10):
        contador +=1
        print("i:", i, "j:", j)
        if contador >50:
            break

print("contador", contador)

``` 


### Continue
Con la instrucción continuar podemos detener la interacción actual y continuar con la siguiente:
``` python
j = 0
for i in range(10):
    j += 2
    print("i:", i, "j:", j )
    if j >=2 and j <=10:
        continue
    print ("El valor de j:", j)
```    




