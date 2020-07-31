# Conjuntos são como listas, mas não possuem index, não aceitam
# valores repetidos e não garantem ordenação.

a = {1, 2, 3}
print(type(a))  # <class 'set'>
b = set('cod3r')
print(b)  # {'c', 'o', 'd', '3', 'r'}
print('3' in a, 4 not in a)  # True True
c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))  # {1, 2, 3}
print(c1.intersection(c2))  # {2}
c1.update(c2)
print(c1)  # {1, 2, 3}
print(c2 <= c1)  # True -> Check whether c2 values is subset of c1
print(c1 >= c2)  # True -> Check whether c1 values is superset of c2
print({1, 2, 3} - {2})  # {1, 3}
c1 -= {2}
print(c1)  # {1, 3}
print(*a)  # 1 2 3
