# Types are dynamic in Python

a = 10
b = 5.2

print(a + b)  # 15.2

c = 4
c = 'Word'
print(c)  # "World"

d = 5
e = d
print(e)  # 5

name, age = 'John', 30
print(name, age)  # John 30

[f, g] = [1, 2]
print(f, g)  # 1 2

h = 10
i = 20

print(h, i)
h, i = i, h  # switch values
print(h, i)
