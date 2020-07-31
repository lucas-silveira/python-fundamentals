print('Nome do módulo', __name__)

# Ao importarmos esse módulo dentro de outro arquivo, a expressão acima
# será executada automaticamente. Para evitarmos que isso aconteça podemos
# usar uma condição que verifica se o arquivo é o principal.

if __name__ == '__main__':
    print('Essa mensagem só é exibida no arquivo principal')


def print_hello(name):
    print(f'Hello {name}!')
