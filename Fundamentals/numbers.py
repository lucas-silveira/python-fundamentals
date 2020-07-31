from decimal import Decimal, getcontext

a = 5
b = 2.5
a / b  # float
a + b  # float
a * b  # float

type(a)  # int
type(b)  # float

b.is_integer()  # False
(-2).__abs__()  # 2
abs(-2)  # 2


print(Decimal(1) / Decimal(7))  # 0.1428571428571428571428571429
getcontext().prec = 2  # set decimal places
print(Decimal(1) / Decimal(7))  # 0.14
print(Decimal.max(Decimal(1), Decimal(7)))  # 7
