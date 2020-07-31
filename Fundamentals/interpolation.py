from string import Template

# Interpolação em Python é substituir valores em uma string. É semelhante ao
# template string do Javascript.
name, age = 'John', 30

# Old Version
print('Nome: %s, Idade: %d' % (name, age))  # Nome: John, Idade: 30
# %s: string
# %d: int
# %f: float
# %.2f: float with 2 decimal places
# %r: boolean


# New Version in Python < 3.6
print('Nome: {0}, Idade: {1}'.format(name, age))  # Nome: John, Idade: 30
# Os números dentro das chaves representam os índices dos argumentos
# dentro do método "format"


# New Version in Python >= 3.6
print(f'Nome: {name}, Idade: {age}')  # Nome: John, Idade: 30

text = Template('Nome: $name, Idade: $age')
print(text.substitute(name=name, age=age))  # Nome: John, Idade: 30
