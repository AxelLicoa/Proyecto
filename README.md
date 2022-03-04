## ¿Qué es Python?![imagen](https://user-images.githubusercontent.com/99735479/156707792-1f4405ab-475c-4f8b-af3b-f71414e0b513.png)
Python, es uno de los muchos lenguajes de progrmación que existe. Lo que hace diferente a python es que tiene un lenguaje interpretado, no hay necesidad de compilarlo para que se lleve acabo las acciones que defines en python, si no que estás se ejecutan directamente por el ordenador.
## ¿Qué es una variable?
Las variables en python pueden estar representadas normalmente por letras, nombres, pronombres, etc... Es donde guardamos los datos ya sea de tipo, str, int o float.
### Nombrando una variable
```python
  Creo una variable de nombre dia
  dia = "Lunes"
  Imprimo el tipo de variable
  print(type(dia))
  dia = 21
  print(dia)
  Para sabe el tipo de variable utilizamos la función type
  print(type(dia))
  dia = 21.5
  print(type(dia))
  ```


### Asignando valores a una variable
``` python
Asignaciones en la misma linea
x=12; y=10; z=4
print('x', x)
print('y', y)
print(z)
print('x=', x, 'y=', y, 'z=', z)
Asignación multiple
dia, mes, anho = "Martes", "Diciembre", 2021
print(dia,mes,anho)
print('Hoy es', dia)
print(', el mes actual es', mes)
print('y el año es', anho)
print('Hoy es', dia, ', el mes actual es', mes, 'y el año es', anho)
Asignación del mismo valor
var1 = var2= 10
Asignación de intercambio
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
``` python
En esta operación el orden de los factores no alera el producto. Le podemos asignar variables a estos números y multiplicarlas.
multiplicacion = num1 * num2
print(num1, 'x', num2, '=',multiplicacion)
Y como el orden de los factores no altera al producto podemos hacerlo de la siguiente forma 
multiplicacion = num2 * num1
print(num2, 'x', num1, '=',multiplicacion)
``` 

### División
``` python
Aquí hay que tener mucho cuidado, no podemos dividir para cero así que no podemos darle 0 a una variable y el orden de los factores si altera al producto. Asignaremos variables y procedemos a efectuar la operación.
num1= 50
num2= 5
division = num1 / num2
print(num1, '/', num2, '=',division)
```
### Módulo
``` python
Operador aritmético que nos sirve para poder obtener el residuo de las divisiones.
num1= 80
num2= 7

mod = num1 % num2
print(num1, '%', num2, '=',mod)
```


## Tipos de datos en Python

### Integer

### Float

### String

## Casting en Python
### Cast
### List

### Tuple

### Dictionary

## Tomando decisiones

### Sentencia if

### Ciclo For

### Ciclo While

### Break

### Continue

