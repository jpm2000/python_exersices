a = [1,2,3,4,5,6]
b = a

print(a)
print(b)

del a[1]

print(a)
print(b)

c = a[:]

print(id(a))
print(id(b))
print(id(c)) # ID en memoria es diferente

a.append(6)

print(id(a))
print(id(b))
print(id(c))

print(a)
print(b)
print(c)