from first_class import double, square


def process(title, list, function):
    print(f'Processando: {title}')
    for i in list:
        print(i, '=>', function(i))


if __name__ == '__main__':
    process('Dobros de 1 a 10', range(1, 11), double)
    process('Quadrados de 1 a 10', range(1, 11), square)
