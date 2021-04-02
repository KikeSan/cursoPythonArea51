



def get_full_name(*args):

  print(f'Este es el primer argumento {args[0]} ')

  return ' '.join([arg for arg in args])

  # "return full name"
  
  #value = f'{name} {father_last_name} {mother_last_name}'
  # return value


print(get_full_name('Kevyn', 'Franco', '28', 'Gato', 'Perro'))


def get_full_name(**kwargs):

  print( f' {kwargs.get("name" )} {kwargs.get("last_name_father")} {kwargs.get("age")} ')


print(get_full_name(

    name='Kevyn',
    last_name_father='Franco',
    age='28'

))


def get_full_name(*args, **kwargs):
  
  for arg in args:
    print(f' Este es un argumento por posicion {arg}')


  for key, value in kwargs.items():

    print(f'la LLave es {key}')
    print(f'El valor es {value}')


get_full_name(1, 'hola', 'Mundo', name='Kevyn', last_name='Franco')



def get_full_name(*args, **kwargs):
  
  for arg in args:
    print(f' Este es un argumento por posicion {arg}')


  for key, value in kwargs.items():

    print(f'la LLave es {key}')
    print(f'El valor es {value}')

  return kwargs.get('name'), kwargs.get('last_name')


name_2, last_name_2 = get_full_name(1, 'hola', 'Mundo', name='Kevyn', last_name='Franco')