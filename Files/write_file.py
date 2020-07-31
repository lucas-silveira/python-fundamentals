from os import path

with open(path.join(path.dirname(__file__), 'persons.csv')) as input_file:
    with open(path.join(path.dirname(__file__), 'persons.txt'), 'w') as \
            output_file:
        for item in input_file:
            [name, age] = item.strip().split(',')
            print(f'Nome: {name}, Idade: {age}', file=output_file)
            # The argument "file" from print function is used for
            # declare the write target. By default is the terminal.

if input_file.closed:
    print('O arquivo de entrada já foi fechado')
if output_file.closed:
    print('O arquivo de saída já foi fechado')
