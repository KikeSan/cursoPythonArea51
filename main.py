

# WHILE

number = 0

while number<=10:
    print(f'El número en memoria es {number}')
    number +=1

print('Salió del bucle')

##############################

print('Ingrese 0 para salir del bucle')
value = int(input('Ingrese elemento: '))

while value!=0:
    print('El elemento es diferente de 0')
    print('Ingrese 0 para salir del bucle')

    if value == 5:
        print('Elemento detectado')
        break  # rompe el loop

    if value == 6:
        print('Elemento detectado')
        continue  # vuelve a ejecutar el bucle sin ejecutar el codigo siguiente

    value = int(input('Ingrese elemento: '))
else:
    print('#'*50)
    print('El elemento ingresado es 0')

##############################



