
# 1) Imprimir “Hola mundo” por pantalla

print('Hola Mundo')

# 2) Crear dos variables numéricas, sumarlas y mostrar el resultado

val1 = 5
val2 = 3
resp = val1 + val2
print('Respuesta:',resp)

print( int.__add__(val1,val2))

# 3) Mostrar el precio del IGV de un producto con un valor de 100 y su precio final.




# 5) Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.

valor = 5
if 0<valor<10:
    print('El valor está entre 0 y 10')

# 6) Añadir al anterior ejercicio, que si esta entre 11 y 20, muestre otro mensaje diferente y si esta entre 21 y 30 otro mensaje.

#valor = int(input('Ingresa una variable: '))
#if valor in range(0,11):
#    print('El valor está entre 0 y 10')
#elif valor in range(11,20):
#    print('El valor está entre 11 y 20')
#elif valor in range(21,30):
#    print('El valor está entre 21 y 30')


# 7) Mostrar con un while los números del 1 al 100.

number = 1
while number in range(0,5):
    print(f'número: {number}')
    number += 1


# 8) Mostrar con un for los números del 1 al 100.
num = 1
for num in range(1,5):
    print(num)


# 9) Mostrar los caracteres de la cadena “Hola mundo”.

for char in 'Hola mundo':
    print(char)

# 10) Mostrar los números pares entre 1 al 100.

   # opcion 1
for i in range(1,101):
    if i % 2 == 0:
        print(i)

    #opcion 2
num = 1
while num <=100:
    if num % 2 == 0:
        print(num)
    num += 1

    #opción del profe
value = [num for num in range(1,101) if num % 2 == 0]
print(value)




# 11) Generar un rango entre 0 y 10

value = [num for num in range(1,11)]
print(value)



# 12) Generar un número entre 5 y 10

import random
print(random.randint(5,10))

# Si solo vamos a usar el metodo randint, hacemos la importación solo de randint
from random import randint
print(randint(5,10))

# 13) Generar un rango de 10 a 0.

value = [num for num in range(0,11)]
value.reverse()
print(value)



# 14) Generar un rango de 0 a 10 y de 15 a 20, incluidos el 10 y 20

value = [num for num in range(0,11)]
value2 = [num for num in range(15,21)]
print(value+value2)

   #opcion del profe
value3 = [num for num in range(0,11)]
value3.extend([num for num in range(15,21)])
print(value3)

# 15) Generar un rango desde 0 hasta la longitud de la cadena “Hola mundo”

value = [num for num in range(0,len('Hola Mundo')+1)]
print(value)

# 16) Pide dos cadenas por teclado, muestra ambas cadenas con un espacio entre ellas y con los 2 primeros caracteres intercambiados. Por ejemplo, hola mundo pasaría a mula hondo

valor1 = input('Ingresa un texto: ')
valor2 = input('Ingresa otro texto: ')

cadena1 = valor2[:2]+valor1[2:]
cadena2 = valor1[:2]+valor2[2:]
print(cadena1+' '+cadena2)
print(f'{valor2[:2]}{valor1[2:]} {valor1[:2]}{valor2[2:]}')

# 17) Pide una cadena e indica si es un palíndromo o no.

chain_1 = input('ingrese palabra')
if chain_1 == chain_1[::-1]:
    print('Es palíndromo')
else:
    print('No es palíndromo')

# 18) Juguemos al juego de adivinar el numero, generaremos un número entre 1 y 100.



# 19) Pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres.



# 20) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.





# 21) Crea una tupla con números e indica el numero con mayor valor y el que menor tenga.





#) 22) Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.




# 23) Crea una lista vacía (pongamos 10 posiciones), pide sus valores y devuelve la suma y la media de los números.
