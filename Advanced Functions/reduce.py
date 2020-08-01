from functools import reduce

persons = [
    {'name': 'Peter', 'age': 24},
    {'name': 'Mary', 'age': 30},
    {'name': 'Jack', 'age': 28},
    {'name': 'Alice', 'age': 34},
    {'name': 'John', 'age': 22},
    {'name': 'Amy', 'age': 31},
]

sum_ages = reduce(lambda accumulator, person: accumulator +
                  person['age'], persons, 0)
print(sum_ages)  # 169
