# Arithmetic Operators
print('[Arithmetic Operators]')
print(2 + 3)  # sum
print(4 - 7)  # sub
print(2 * 5.3)  # multi
print(9.3 / 3)  # division -> result is float type
print(9 // 3)  # division -> result is rounded and int type
print(2 ** 8)  # potency
print(10 % 3)  # module


# Relational Operators
print('\n[Relational Operators]')
print(3 > 4)  # False
print(3 < 4)  # True
print(3 >= 4)  # False
print(3 <= 4)  # True
print(3 == 4)  # False
print(3 != 4)  # True

# Assignment Operators
a = 3  # 3
a = a + 7  # 10
a += 5  # 15
a -= 3  # 12
a *= 2  # 24
a /= 4  # 6
a %= 4  # 2
a **= 8  # 256
a //= 256  # 1


# Logic Operators
print('\n[Logic Operators]')
print(True or False)  # True
print(7 != 3 and 2 > 3)  # False
print(not True)  # False
print(not False)  # True
print(not not "string")  # True
print(not not "")  # False


# Ternary Operators
print('\n[Ternary Operators]')

# First method
result = ('case false', 'case true')[True]
print(result)  # case true

itsRaining = True
print('Today I have ' + ('dry', 'wet')[itsRaining] + ' clothes')

# Second method
result = ('case true' if True else 'case false')
print(result)  # case true


# Member and Entity Operators
print('\n[Member and Entity Operators]')

# Member
list = [1, 2, 3, 'Alice', 'Carl']
print(2 in list)  # True
print('Alice' not in list)  # False

# Entity
x = 3
y = x
z = 3
print(x is y)  # True
print(y is z)  # True
print(y is not z)  # False

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print(list_b is list_a)  # True
print(list_b is list_c)  # False
print(list_a is not list_c)  # True
