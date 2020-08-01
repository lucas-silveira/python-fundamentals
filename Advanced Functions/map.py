list_1 = [1, 2, 3]
double = list(map(lambda x: x * 2, list_1))
print(double)  # [2, 4, 6]


list_2 = [
    {'name': 'John', 'age': 31},
    {'name': 'Mary', 'age': 37},
    {'name': 'Peter', 'age': 26},
]
names_only = list(map(lambda person: person['name'], list_2))
print(names_only)  # ['John', 'Mary', 'Peter']

ages_only = list(map(lambda person: person['age'], list_2))
print(ages_only)  # [31, 37, 26]
print(sum(ages_only))  # 94
