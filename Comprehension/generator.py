import sys
from list_comprehension import doubles_of_evens

# The generator generates data on demand that is it does not load
# the entire list into memory
generator = (i ** 2 for i in range(10) if i % 2 == 0)

print(next(generator))  # 0
print(next(generator))  # 4
print(next(generator))  # 16
print(next(generator))  # 36
print(next(generator))  # 64
# print(next(generator))  # error
print(next(generator, 'No more values'))  # prevent error

print(sys.getsizeof(doubles_of_evens))  # size 120
print(sys.getsizeof(generator))  # size 112


generator2 = (i ** 2 for i in range(10) if i % 2 == 1)
# with for loop
for number in generator2:
    print(number)

# If We had used the first generator the print function would not
# display anything because the first generator was already read
