# Tuplas em Python são como as listas, porém elas não podem ser modificadas.

tupla = tuple()  # create a tuple
tupla = ()  # create a tuple

tupla = ('um',)  # create a tuple with 1 element.
print(tupla[0])  # um
print(tuple(range(0, 7)))  # (0, 1, 2, 3, 4, 5, 6)

cores = ('red', 'green', 'blue')
print(cores)  # ('red', 'green', 'blue')
print(cores.index('green'))  # 1
print(cores.count('blue'))  # 1

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # (1, 2, 3, 4)

# Tuples accept range index
print(cores[1:])  # ('green', 'blue')

# Desestruturando os valores da tupla em argumentos da função.
print(*cores)  # red green blue
# O asterísco (*) é semelhante ao reticências (...) do Javascript
# para desestruturar arrays e objetos

# Join two lists/tuples with pairs
list5 = [1, 2, 3]
list6 = [4, 5, 6]
together = zip(list5, list6)
print(tuple(together))  # ((1, 4), (2, 5), (3, 6))
