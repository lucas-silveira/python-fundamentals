import os

try:
    file = open(os.path.join(os.path.dirname(__file__), 'persons.csv'))

    for item in file:
        [name, age] = item.strip().split(',')
        print(f'Nome: {name}, Idade: {age}')

except IndexError:
    # The statements bellow will be called when the block above
    # throws an error of type IndexError
    pass

finally:
    # The statements bellow will be called even if the try block
    # throws an error
    file.close()

if file.closed:
    print('O arquivo já foi fechado')
