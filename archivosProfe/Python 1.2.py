# Tupla
tupla = (1, 2, 3, 4)

tupla.count(1)


tupla.index(1)

# tupla.append() - No existe


tupla = list(tupla)

#Diccionario -> Json

dictt = {
  'name': 'Kevyn',
  'age': 10,
  'average': 19.9,
  'other': [
    'Hola', 'Mundo'
  ],
  'other2': ('Hola', 'Mundo'),
  'books': {
    'name': 'Pytho'
  }
}

dictt['name']
# dictt['name2']
dictt.get('name2', None)

dictt['name'] = 'Franco'
dictt['name2'] = 'Kevyn'

dictt.keys() # -> Recuperar Llaves
dictt.values()

# dictt.clear() # -> Eliminar todos los elementos internos


# dictt_2 = dictt -> Referencia

dictt_2 = dictt.copy()

keys = ('name', 'last_name', 'age') 
dictt_3 = dict.fromkeys(keys)

dictt_4 = dictt_3.fromkeys(('name', 'age'))

# dictt_3.has_key('name') -> Dato Curioso


dictt_4.items()

# dictt_4.pop()


# b'' - import json    /.  json.loads(b'')


# Codicionales


if 5 == 3:
  print('Es igual')

elif 5 != 5:
  print('Es diferente')

elif 5 != 5:
  print('Es diferente')

elif 5 != 5:
  print('Es diferente')

else:
  print('No cumple ninguna condicion anterior')


# if 1 is '1':
#   print('Es correcto')


lista = ['hola', 'mundo', 1, 2, 3]

tupla = ('hola', 'mundo', 1, 2, 3)

if 'hola' in lista:
  print('Si existe elemento')


if 'Python' not in lista:
  print('No esta dentro de la lista')


dictt = {
  'name': 'Kevyn'
}

if dictt.get('name'):
  print('hola Mundo')


if dictt.get('last_name'):
  print('hola Mundo')


if not dictt.get('last_name'):
  print('hola Mundo')


# and. or

name = dictt.get('name')
if not dictt.get('last_name') and  name:
  print(name)


# || &&
name = dictt.get('name')
if dictt.get('last_name') or  name:
  print(name)

#Iteradores



number = 0

while number <= 10:
  print(f'El numero en memoria es {number}')
  number +=1

print('Salio')


#################### 



print('Ingrese 0 para salir del blucle')
value = int(input('Ingrese Elemento: '))

while value != 0:
  print('El elemento es diferente de 0')
  print('Ingrese 0 para salir del blucle')

  if value == 5:
    print('Elemento detectado')
    break
  elif value == 6:
    print('Nuevo elemento detectado')
    continue

  value = int(input('Ingrese Elemento: '))
else:
  print('#' * 50)
  print('El elemento ingreso es 0')



number = 0

while number <= 10: # 3 #6 # 9
  print(number)
  # value = 6
  if value != 6: 
    print(f'El numero en memoria es {number}')
  else: # 1 # 4 # 7
    print('Ya no ejecuta nada mas a partir de este punto')
    continue # 2 #5 #8
  
  number +=1

print('Salio')
