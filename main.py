# Listas
value = [1,2,3,4,5,6.0,'7.0',[8,9,'10']]

print(value[0])
print(value[5])
print(value[7][0])
print(len(value))

print(value[-1])

value[-1] = 8
print(value)

value.append(9)
value.append(9)
value.append([10,11,12])
print(value)

print(value.count(9))

print(value)

value.extend([13,14,15])

print(value)

value.extend('Hola Mundo')
print(value)

value.extend(range(1,101))
print(value)

# range(1,10) -> [1,2,3 ... 9]

print(value.index(5))

value.insert(0,0)
print(value)

value.pop()
print(value)

value.remove(1)
print(value)

value.reverse()
print(value)

"""
value = [1,3,5,2,4]
value.sort()
print(value)
value.sort(reverse=True)
print(value)
"""

value[-5:]
print(value)