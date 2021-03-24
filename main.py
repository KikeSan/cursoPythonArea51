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

# WHILE

