# No modo stream, não carregamos o arquivo na memória, ou seja,
# o arquivo é lido sob demanda através do laço de repetição.
import os

file = open(os.path.join(os.path.dirname(__file__), 'persons.csv'))

for item in file:
    [name, age] = item.strip().split(',')
    print(f'Nome: {name}, Idade: {age}')

file.close()

if file.closed:
    print('O arquivo já foi fechado')
