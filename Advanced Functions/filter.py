persons = [
    {'name': 'Peter', 'age': 24},
    {'name': 'Mary', 'age': 30},
    {'name': 'Jack', 'age': 28},
    {'name': 'Alice', 'age': 34},
    {'name': 'John', 'age': 22},
    {'name': 'Amy', 'age': 31},
]

bigger_than_thirty = list(filter(lambda person: person['age'] >= 30, persons))
print(bigger_than_thirty)
# [{'name': 'Mary', 'age': 30}, {'name': 'Alice', 'age': 34}, {'name': 'Amy', 'age': 31}]


big_names = list(filter(lambda person: len(person['name']) > 4, persons))
print(big_names)
# [{'name': 'Peter', 'age': 24}, {'name': 'Alice', 'age': 34}]
