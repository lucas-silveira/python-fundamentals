dictionary = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dictionary)

dictionary2 = {f'Item {i}': i * 2 for i in range(10) if i % 2 == 0}
print(dictionary2)


for key, value in dictionary.items():
    print(f'{key} x 2 = {value}')
