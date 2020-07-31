# Em Python as listas são dinâmicas e heterogêneas
# (como os arrays em Javascript)

print('[Manipulating lists]')

list = []
print(list)  # []
print(len(list))  # 0
print(list.count(1))  # 0
list.append(1)
print(list)  # [1]
print(len(list))  # 1
print(list.count(1))  # 1

list2 = [1, 2, 'John', 'Alice']
list2.remove(2)  # remove by value
print(list2)  # [1, 'John', 'Alice']
list2.reverse()
print(list2)  # ['Alice', 'John', 1]
del list2[2]  # remove by index
print(list2)  # ['Alice', 'John']


print('\n[Accessing lists]')

# Acessing by index or value
list3 = ['John', 'Alice', 'Peter']
print(list3.index('Alice'))  # 1
print('Piter' in list3)  # True
# print(list3.index('Ben'))  # Error
print(list3[2])  # Peter
print(list3[-1])  # Peter


print('\n[Get values range]')

print(list3[:])  # ['John', 'Alice', 'Peter']
print(list3[:2])  # ['John', 'Alice']
print(list3[1:])  # ['Alice', 'Peter']
print(list3[1:3])  # ['Alice', 'Peter']
print(list3[-1:])  # ['Peter']
print(list3[::])  # ['John', 'Alice', 'Peter']
print(list3[::2])  # ['John', 'Peter']
print(list3[1::2])  # ['Alice']
print(list3[::-1])  # ['Peter', 'Alice', 'John']
print(list3[::-2])  # ['Peter', 'John']

del list3[1:]  # delete by range index
print(list3)  # ['John']


print('\n[Destructuring values]')

list4 = [1, 2, 3]
print(*list4)  # 1 2 3
