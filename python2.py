# TUPLA
# Las tuplas son más rápidas en ejecutar que las listas

tupla = (1,2,3,4)
print(tupla)
print(type(tupla))

print(tupla.count(1))
print(tupla.index(1))

""" 
a las tuplas no se les puede agregar elementos
convertimos la tupla en lista para poder usar append
"""
tupla = list(tupla)
print(type(tupla))
tupla.append(5)
tupla = tuple(tupla)
print(tupla)
print(type(tupla))

# DICCIONARIO -> Json

dictt = {
    'name':'Kike',
    'age':38,
    'average':19.9,
    'other':[
        'Hola','Mundo'
    ],
    'other2':('Hola','Mundo'),
    'books':{
        'name':'Pytho'
    }
}

# No se recomienda este tipo
print(dictt['name'])
# en su lugar usar get, de este modo no arroja error al no encontrar la llave
print(dictt.get('name'))
# se le puede pasar un segundo parametro en caso no encuentre la llave
print(dictt.get('name2','Default'))

dictt['name'] = 'Franco'
print(dictt)

dictt['name2'] = 'Kevyn'
print(dictt)

#recuperar llaves
print(dictt.keys())

#recuperar Valores
print(dictt.values())

# Elimina todos los elementos del diccionario
# dictt.clear()

dictt2 = dictt  # referencia

print(dictt2)
dictt['name']='Francisco'
print(dictt)
print(dictt2)

dictt_2 = dictt.copy()
print(dictt_2)
dictt['name']='Kike'
print(dictt)
print(dictt_2)

# transformar una tupla a un diccionario

""""
keys = ('name','last_name','age')
dictt_3 = dictt.fromkeys(keys)
print(dictt_3)
"""

keys = ('name','last_name','age')
dictt_3 = dict.fromkeys(keys)
print(dictt_3)

dictt_4 = dictt_3.fromkeys(('name','age'))
print(dictt_4)

print(dictt_4.items())

dictt_4.pop('name')
print(dictt_4)


# CONDICIONALES & OPERADORES RACIONALES

if 5 == 5:
    print('es igual')

elif 5 != 3:
    print('Es diferente')

elif 5 != 2:
    print('Es diferente')

elif 5 != 1:
    print('Es diferente')

else:
    print('No cumple ninguna condicion')

# El is es equivalente al === de js
#if 1 is 1:
#    print('Es correcto')

lista = ['hola','mundo',1,2,3]
if 'hola' in lista:
    print('Si existe el elemento')

if 'Python' not in lista:
    print('No está en la lista')

dictt = {
    'name':'Kike'
}
if dictt.get('name'):
    print('Hola Mundo')

if dictt.get('last_name'):
    print('Hola Mundo')

if not dictt.get('last_name'):
    print('Hola Mundo')

# and or

name = dictt.get('name')
if not dictt.get('last_name') and name:
    print(name)


name = dictt.get('name')
if dictt.get('last_name') or name:
    print(name)