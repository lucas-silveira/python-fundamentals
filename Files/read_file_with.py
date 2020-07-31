import os

# Through the expression "with" the file will be closed automatically.
# This resource also can to use with others things,
# for example an request http function.
with open(os.path.join(os.path.dirname(__file__), 'persons.csv')) as file:
    for item in file:
        [name, age] = item.strip().split(',')
        print(f'Nome: {name}, Idade: {age}')

if file.closed:
    print('O arquivo já foi fechado')
