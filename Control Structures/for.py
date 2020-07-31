# O laço for pode percorrer: range,string, lista, tupla, set e dicionários.

print('[Range]')
for i in range(1, 11):
    print(f'i = {i}')

for j in range(10):
    print(f'j = {j}')


print('\n[String]')
word = 'cod3r'
for letter in word:
    print(letter, end=',')


print('\n[List]')
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)

for index, name in enumerate(fruits):
    print(index, name)


print('\n[Dictionaries]')
product = {'name': 'Caneta', 'price': 14.99, 'imported': True, 'stock': 793}
for key in product:
    print(key)

for value in product.values():
    print(value)

for key, value in product.items():
    print(key, '=', value)

print(key, value)  # Os valores continuam disponíveis fora do bloco


print('\n[For with Else')
for i in range(10):
    print(i)
else:
    print('End')
# O else não será executado caso o loop se depare com um break
