value = 1

print(type(value)) #-> print ''


value = 1.0



print(type(value))



value = True #-> 1 / 0



print(type(value))



## value = (1, 2, 3, 4) -> (1, )

# 1.0 

print('Hola ' + 'Mundo')

# 2.0 - 3.5

print('Hola {} estoy aprendiendo {}'.format('Mundo', 'Python'))

print('Hola {text_1} estoy aprendiendo {text_2}'.format(text_1='Mundo', text_2='Python'))


print('Hola {0} estoy aprendiendo {1}'.format('Mundo', 'Python'))


# 3.6 > 

text = 'Mundo'

print(f'Hola {text}')


# Constantes

None # -> Null
# NotImplement #-> noimplementadas
True # -> 1
False # -> 0

if
elif
else

and
or

for
while
else


try
except

pass
continue

del 


 def #->
 lambda #-> 

import constants 

print(constants.URL_API_GOOGLE)

from constants import URL_API_GOOGLE

print(URL_API_GOOGLE)





# Operador Asigancion
r = 5
# r = r + 10

print(r)

r += 10 
print(r)
r -=10
print(r)
r *=10
print(r)
r /= 10
print(r)
r %= 10
print(r)

# 
value = 3 + 4 

value = 3 - 4
# ...

print(value)

value = int.__add__(3, 4)


# Operadores racional
5 == 3 
5 != 3
5 > 3
5 < 3
5 >= 3
5 <= 3


# long = 42L
# int
# float 1.1424232132312323123 + 1.134545454545545


value = 2
print(type(value))


value = float(2)

print(type(value))


value = int(2)


print(type(value))


value = str(2)


print(type(value))


value = '2'
value = int(value)

print(type(value))

value = 'H'

value = int(value)


# value = 2.1 + 7.8j

# Listas
value = [1, 2, 3, 4, 5, 6.0, '7.0', [8, 9, '10']]


print(value[0])

print(value[5])

print(value[7][0])


print(len(value))

print(value[-1])


value[-1] = 8

print(value)


value.append(9)

value.append(9)


value.append([10, 11, 12])

print(value)




print(value.count(9))


print(value)

value.extend([13, 14, 15])

print(value)

value.extend('Hola Mundo')

print(value)

value.extend(range(1, 101))

print(value)

# range(1, 10) -> [1, 2, 3 .... 9] range(1, 101)

print(value.index(1))



value.insert(0, 0)


print(value)
""" 

value.pop()


value.remove(1)


value.reverse()

""" 

# value.sort()


# value.sort(reverse=True)


# range(1, 5) -> [1, 2, 3, 4]

value.extend(range(5,9))