print('[Text with multiple lines]')
text = '''First line...
Second line...
End...'''
print(text)


print('\n[Accessing caracters through the index]')
name = 'Jim Carrey'
print(name[0])  # J
print(name[-1])  # y
print(name[:])  # Jim Carrey
print(name[4:])  # Carrey
print(name[-3:])  # rey
print(name[:3])  # Jim
print(name[2:3])  # m

numbers = '1234567890'
print(numbers[::])  # 1234567890
print(numbers[::2])  # 13579
print(numbers[1::2])  # 24680
print(numbers[::-1])  # 0987654321
print(numbers[::-2])  # 08642


print('\n[Members]')
print('Jim' in name)  # True
print('jim' in name)  # False


print('\n[Other methods]')
print(name.lower())  # jim carrey
print(name.upper())  # JIM CARREY
print(len(name))  # Number of characters: 10
print(name.split(' '))  # ['Jim', 'Carrey']
name2 = '000Natalie Portman000'
print(name2.strip('0'))  # Natelie Portman
# strip remove space blanks by default
print('&'.join(['1', '2', '3']))  # 1&2&3

print(r'\n\n\n')  # \n\n\n
# This literally prints the string without exceptions
