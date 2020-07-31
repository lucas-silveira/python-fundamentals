def duble(x):
    return x * 2


def square(x):
    return x ** 2


if __name__ == '__main__':
    d = duble
    s = square
    print(d(5))  # 10
    print(s(5))  # 25

    funcs = [duble, square] * 5  # repeat the list 5 times

    for func, number in zip(funcs, range(1, 11)):
        print(f'O {func.__name__} de {number} é {func(number)}')
