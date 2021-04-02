

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