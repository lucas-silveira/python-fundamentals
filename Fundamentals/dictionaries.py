# Dicionários em Python são parecidos com os objetos em Javascript.
# Possuem uma chave (key) normalmente no formato de string, e um valor
# que pode ser de qualquer tipo.

print('[Accessing values]')
person = {
    'name': 'Teacher Alice',
    'age': 38,
    'courses': ['English', 'Portuguese']
}
print(type(person))  # <class 'dict'>
print(person)
# {'name': 'Teacher Alice', 'age': 38, 'courses': ['English', 'Portuguese']}
print(person['name'])  # Teacher Alice
print(person.get('age'))  # 38
print(person.get('tags', []))  # []
print(person['courses'][0])  # English
print(len(person))  # Quantity of keys
print(person.keys())  # dict_keys(['name', 'age', 'courses'])
print(person.values())
# dict_values(['Teacher Alice', 38, ['English', 'Portuguese']])


print('\n[Manipulating values]')
person['age'] = 30
person['courses'].append('Spanish')
print(person)
# {'name': 'Teacher Alice', 'age': 30, 'courses': ['English', 'Portuguese', 'Spanish']}
person.pop('age')  # remove and return value
print(person)
# {'name': 'Teacher Alice', 'courses': ['English', 'Portuguese', 'Spanish']}
person.update({'age': 40, 'gender': 'female'})
print(person)
# {'name': 'Teacher Alice', 'courses': ['English', 'Portuguese', 'Spanish'], 'age': 40, 'gender': 'female'}
del person['courses']
print(person)  # {'name': 'Teacher Alice', 'age': 40, 'gender': 'female'}
person.clear()
print(person)  # {}

person2 = {
    'name': 'Teacher John',
    'age': 32,
    'courses': ['English', 'Spanish']
}
print(*person2)  # name age courses
print(*person2.values())  # Teacher John 32 ['English', 'Spanish']

# Join two lists/tuples with pairs
list5 = [1, 2, 3]
list6 = [4, 5, 6]
together = zip(list5, list6)
print(dict(together))  # {1: 4, 2: 5, 3: 6}
