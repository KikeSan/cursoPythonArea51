
############################


# For

# lista = [] -> list()
# tupla = () -> tuple()
# dict = {} -> dict()

lista = list() # []
lista.append(1)
lista.append(2)
lista.append(3)

for num in lista:
  print(num)

print('Tupla')
for num in tuple(lista): # -> (1, 2, 3)
  print(num) 

for char in 'hola mundo':
  print(char)

dictt_value = {
  'name': 'Kevyn',
  'last_name': 'Franco'
}

# dictt_value.keys()
# dictt_value.values()
# dictt_value.items()
for key, value in dictt_value.items():
  print(key)
  print(value)


# value = 'Hola'
# value_2 = 'Mundo'

# value, value_2 = 'Hola', 'Mundo'


# 1) Imprimir “Hola mundo” por pantalla
print('Hola Mundo')

saludo = 'Hola Mundo!'
print(saludo)

# 2) Crear dos variables numéricas, sumarlas y mostrar el resultado

x = 120
y = 45
print(y+x)

print(int.__add__(x, y))


# 3) Mostrar el precio del IGV de un producto con un valor de 100 y su precio final.

precio = 100
IGV = 0.18
print((precio) + precio * IGV)

print(precio + (precio * IGV))

# 5) Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.

value = int(input('Ingresa una variable: '))
if value in range(0,11):
  print('Tu número está en el rango de 0 y 10!')
else:
  print('Tu número no cumple con los requisitos')

value = int(input('Ingresa una variable: '))

while True :

  if value in range(0, 11):
    print('Tu numero esta dentro del rango')
    break
  else:
    print('Tu numero no esta en el rango')
    value = int(input('Ingresa una variable: '))

# 6

value = int(input('Ingresa una variable: '))
if value in range(0,11):
  print('Tu número está en el rango de 0 y 10!')
elif value in range(11, 21):
  print('Tu número está en el rango de 11 y 20!')
elif value in range(21, 31):
  print('Tu número está en el rango de 21 y 31!')
else:
  print('Tu número no cumple con los requisitos')


  
# 7) Mostrar con un while los números del 1 al 100.

value = 0

while value != 101:

  print(value)
  value += 1

# 8) Mostrar con un for los números del 1 al 100.

for num in range(1, 101):
  print(num)




# 9) Mostrar los caracteres de la cadena “Hola mundo”.

for char in 'Hola mundo':
  print(char)


# 10) Mostrar los números pares entre 1 al 100.

for i in range(1,101):
  if i % 2 == 0:
    print(i)

num = 1
while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1


# [num for num in range(1, 101) if num % 2 == 0]

# 11) Generar un rango entre 0 y 10

value = [num for num in range(1, 11)]
# value.append(num)

# 12) Generar un número entre 5 y 10

# value = [num for num in range(5, 11)]

# import random
from random import randint

print(randint(5, 10)) #-> aleatorio



# 13) Generar un rango de 10 a 0.

for num in range(10, 0):
  print(num)

value = [num for num in range(0, 11)]
value.reverse()


# 14) Generar un rango de 0 a 10 y de 15 a 20, incluidos el 10 y 20

value = [num for num in range(0, 11)]
value.extend([num for num in range(15, 21)])


value2 = [[num for num in range(0,11)], [num for num in range(15,21)]]

# 15) Generar un rango desde 0 hasta la longitud de la cadena “Hola mundo”

value = [num for num in range(0, len('Hola Mundo') + 1)]



# 16) Pide dos cadenas por teclado, muestra ambas cadenas con un espacio entre ellas y con los 2 primeros caracteres intercambiados. Por ejemplo, hola mundo pasaría a mula hondo

# chain_1 = input('Ingrese primer texto: ')
# chain_2 = input('Ingrese segundo texto: ')

text1 = input('Ingrese el primer texto: ')

while len(text1) < 2:
    print('El texto debe tener más de dos caracteres')
    text1 = input('Ingrese el primer texto: ')

text2 = input('Ingrese el segundo texto: ')
while len(text2) < 2:
    print('El texto debe tener más de dos caracteres')
    text2 = input('Ingrese el segundo texto: ')

print(f'{text2[:2]}{text1[2:]} {text1[:2]}{text2[2:]}')




# 17) Pide una cadena e indica si es un palíndromo o no.
chain_1 = input('Ingrese primer texto: ')

if chain_1 == chain_1[::-1]:
  print('es palindromo')
else:
  print('no es palindromo')


# 18) Juguemos al juego de adivinar el numero, generaremos un número entre 1 y 100.




# 19) Pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres.


value = input('Ingrese Cadena de Texto: ')
sets = {char for char in value}

print(list(sets))
# 20) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.


value = (1, 2, 3, 4 , 5)

number = int(input('Ingrese Numero:'))

print(value.count(number))









# 21) Crea una tupla con números e indica el numero con mayor valor y el que menor tenga.

value = int(input('Ingrese Numero : '))
tupla = list()

while value != 0:

  tupla.append(value)

  value = int(input('Ingrese Numero : '))

else:
  print('Se termino de agregar elementos')


tupla.sort()

tupla = tuple(tupla)

print(f'El menor elemento es {tupla[0]} y el mayor elemento {tupla[-1]}')

#) 22) Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.

contacts = []

while True:
  user = input('Ingrese Nombre de Usuario: ')
  phone = input('Ingrese numero de telefono: ')

  exists = False
  for element in contacts:
    if element.get('user') == user:
      print('El usuario ya existe')
      exists = True
      break

  if exists:    
    continue

  contacts.append({
    'user': user,
    'phone': phone
  })

  validator = input('Desea Continuar? Si/No')

  if validator.lower() == 'no':
    break

print(contacts)





# 23) Crea una lista vacía (pongamos 10 posiciones), pide sus valores y devuelve la suma y la media de los números.

lista = [1, 2, 3, 4,  5, 6]

suma = sum(lista)

media = suma/len(lista)

print(f'La suma de los elementos es {suma}, y la media de los elementos es {media}')


##########################. 

def get_full_name(name, last_name_father, last_name_mother=''):
  """ return a full_name """

  value = f'{name} {last_name_father} {last_name_mother}'

  return value



print(  get_full_name( 'Kevyn', last_name_father='Franco')  )

print(    get_full_name('Kevyn', 'Franco')     )



print(    get_full_name(
name='Kevyn', last_name_father='Franco', last_name_mother='Caldas')     )





def get_full_name(name, father_last_name, mother_last_name=''):
  "return full name"
  value = f'{name} {father_last_name} {mother_last_name}'
  return value




print (get_full_name('Marcela', father_last_name='Valladares'))

print(get_full_name('Marcela','Valladares'))


print('#' * 58)