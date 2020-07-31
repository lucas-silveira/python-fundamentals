import os

file = open(os.path.join(os.path.dirname(__file__), 'persons.csv'))
data = file.read()
file.close()


for item in data.splitlines():
    [name, age] = item.split(',')
    print(f'Nome: {name}, Idade: {age}')
